from lxml import html
import requests
import json
# Define the URL of the web page you want to scrape
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
def get_sellers(siteurl) :
    dict_sellers = {} 
    response = requests.get(siteurl, headers=HEADERS) 
    if response.status_code == 200:
        print(response.status_code)
        page_content = response.content
        page_content_dict = json.loads(page_content.decode('utf-8'))
        offers = (page_content_dict.get('content').get('offers').get('offers'))
        for offer in offers :
            seller = offer.get('aboutSeller')
            offer_info = offer.get('aboutOffer')
            price = offer.get('aboutPrice')

            dict_sellers[seller.get('sellerDisplayName')] = {"seller_rating" : offer.get('sellerRating').get("rating").get("sellerRating") , "price" : price.get('price') ,
                                                              "condition" : offer_info.get('condition')}
        return dict_sellers
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
def get_all_sellers_info(url) :
    
    # Make a request
    response = requests.get(url, headers=HEADERS)

    # Check the status code
    if response.status_code == 200:
        print(response.status_code)

        page_content = response.content
        parsed_content = html.fromstring(page_content)
        all_sellers_url = parsed_content.xpath('//a[@data-label="all-sellers"]/@href')
        
        if (len(all_sellers_url) > 0) : 
            all_sellers_url = "https://www.bol.com" +  all_sellers_url[0]
            return get_sellers(all_sellers_url)
        
        
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
