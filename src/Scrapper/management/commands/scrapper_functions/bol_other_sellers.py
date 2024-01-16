import requests
from lxml import html

def get_sellers(siteurl, headers):
    dict_sellers = {}
    response = requests.get(siteurl, headers=headers)

    if response.status_code == 200:
        page_content = response.content
        parsed_content = html.fromstring(page_content)
        other_sellers = parsed_content.xpath('//ul[@id="offers"]/*')

        for seller in other_sellers :
            about_seller_block = seller.xpath('.//div[@data-test="about-seller-block"]')
            about_offer_block = seller.xpath('.//div[@data-test="about-offer-block"]')
            about_price_block = seller.xpath('.//div[@data-test="about-price-block"]')
            seller_name = about_seller_block[0].xpath('.//p/*')[0].text_content()
            seller_price = about_price_block[0].xpath('.//span[@class="h-nowrap product-prices__bol-price"]')[0].text_content().replace('\n','').replace(' ','')
            offer_condition = about_offer_block[0].xpath('.//div[@class="about-offer-condition"]//strong')[0].text_content()
            seller_rating = seller.xpath('.//div[@data-test="seller-rating"]')[0].text_content().replace('\n','').replace(' ','')
            # print([seller_name,seller_price,offer_condition,seller_rating])
            dict_sellers[seller_name] = {"seller_rating": seller_rating,"seller_price" : seller_price,"condition" : offer_condition}

        return dict_sellers
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def get_all_sellers_info(url, headers):
    # Make a request
    response = requests.get(url, headers=headers)

    # Check the status code
    if response.status_code == 200:
        print(response.status_code)

        page_content = response.content
        parsed_content = html.fromstring(page_content)
        all_sellers_url = parsed_content.xpath('//a[@data-label="all-sellers"]/@href')

        if (len(all_sellers_url) > 0):
            all_sellers_url = "https://www.bol.com" + all_sellers_url[0]
            return get_sellers(all_sellers_url)
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
