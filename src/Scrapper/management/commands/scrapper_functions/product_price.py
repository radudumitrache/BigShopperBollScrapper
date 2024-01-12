from lxml import html
import requests

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


def get_product_price(url):
    # Make a request
    response = requests.get(url, headers=HEADERS)

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
            return (price, old_price)
        else:
            return price

    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
        # Add your logic here for what to do when the status is not 299