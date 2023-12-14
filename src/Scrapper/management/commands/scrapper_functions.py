from lxml import html
from urllib.parse import urlparse
import requests
import re
import json
# Define the URL of the web page you want to scrape
URL = "https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/?bltgh=hv-IEzy4P-OI9nskywJCaA.2_18.22.ProductTitle"
HEADERS = {
    'authority': 'spoor.bol.com',
    'method': 'GET',
    'path': '/app/v1/config/iylvyb75XjFdC2iUCNMO18sUE4lEXmnQCPCwOozu',
    'scheme': 'https',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://www.bol.com',
    'Referer': 'https://www.bol.com/',
    'Sec-Ch-Ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36'
}

def clean_text(text):
    text = text.replace("\n", " ")
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def web_request(url, headers):
    response = requests.get(url, headers)
    return response

def product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
    }
    response = web_request(url, headers)
    if response.status_code == 200:
        results = dict()
        tree = html.fromstring(response.content)
        specs = tree.xpath('.//div[@class="specs"]/dl[@class="specs__list"]/div[@class="specs__row"]')
        for spec in specs:
            spec_title = spec.xpath('.//dt[@class="specs__title"]/text()')
            spec_value = spec.xpath('.//dd[@class="specs__value"]')
            if spec_title and spec_value:
                results[spec_title[0].strip()] = clean_text(spec_value[0].text_content().strip())

        json_string = json.dumps(results, indent=4)
        return json_string
    else:
        print("Error: ", response.status_code)
        return None

def get_sellers(siteurl):
    dict_sellers = {}
    response = requests.get(siteurl, headers=HEADERS)
    if response.status_code == 200:
        print(response.status_code)
        page_content = response.content
        page_content_dict = json.loads(page_content.decode('utf-8'))
        offers = (page_content_dict.get('content').get('offers').get('offers'))
        # print (offers[0])
        for offer in offers:
            seller = offer.get('aboutSeller')
            offer_info = offer.get('aboutOffer')
            price = offer.get('aboutPrice')
            # print (seller.get('sellerDisplayName'))
            # print (f"{seller.get('sellerDisplayName')} - {price.get('price')}")
            dict_sellers[seller.get('sellerDisplayName')] = {
                "seller_rating": offer.get('sellerRating').get("rating").get("sellerRating"),
                "price": price.get('price'),
                "condition": offer_info.get('condition')}
        return dict_sellers
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


def get_all_sellers_info(url):
    # Make a request
    response = requests.get(url, headers=HEADERS)

    # Check the status code
    if response.status_code == 200:
        print(response.status_code)

        page_content = response.content
        parsed_content = html.fromstring(page_content)
        all_sellers_url = parsed_content.xpath('//a[@data-label="all-sellers"]/@href')

        if (len(all_sellers_url) > 0):
            all_sellers_url = "https://www.bol.com" + all_sellers_url[0]
            return get_sellers(all_sellers_url)
        else :
            return "No other sellers"

    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
        # Add your logic here for what to do when the status is not 299
def get_country_code(url_to_scrape):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url_to_scrape)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # split url by '/' and get second element for country code
            parsed_url = urlparse(url_to_scrape)
            path_components = parsed_url.path.split('/')

            # Check the country code based on the path
            if len(path_components) > 2:
                if path_components[2] == "nl":
                    country_code = "NL"
                elif path_components[2] == "be":
                    country_code = "BE"
                else:
                    country_code = "N/A"
            else:
                country_code = "N/A"

            return country_code

        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
def get_product_name(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            parsed_content = html.fromstring(response.content)

            # Specify XPath expressions for name and URL
            xpath_name = '//span[@class="u-mr--xs"]/text()'

            # Extract data using specified XPaths
            name = parsed_content.xpath(xpath_name)[0] if parsed_content.xpath(xpath_name) else "N/A"

            return name #,url_to_parse //ONLY if we want to return the url to be scraped

        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
def get_product_price(url):
    # Make a request
    response = requests.get(URL, headers=HEADERS)

    # Check the status code
    if response.status_code == 200:
        print(response.status_code)

        page_content = response.content

        parsed_content = html.fromstring(page_content)

        price_content = parsed_content.xpath('//span[@class="promo-price"]')
        price = ""
        for element in price_content:
            print(element.text_content())
            price += element.text_content().replace('\n', '.').replace(' ', '')
        price = price.replace('-', '0')
        price = float(price[:-1])
        print(float(price))
        old_price_content = parsed_content.xpath(
            '//div[starts-with(@class, "ab-discount")]/del[@data-test="list-price"]')
        if (len(old_price_content) > 0):
            old_price = old_price_content[0].text_content().replace(',', '.')
            print(old_price)
            return {"current_price": price , "old_price" : price}
        else:
            return price

    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
        # Add your logic here for what to do when the status is not 299