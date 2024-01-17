from lxml import html
import requests

def get_product_price(url, headers):
    # Make a request
    response = requests.get(url, headers=headers)

    # Check the status code
    if response.status_code == 200:
        page_content = response.content

        parsed_content = html.fromstring(page_content)

        price_content = parsed_content.xpath('//span[@class="promo-price"]')
        price = ""
        for element in price_content:
            # print(element.text_content())
            price += element.text_content().replace('\n', '.').replace(' ', '')
        price = price.replace('-', '0')
        price = float(price[:-1])

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
