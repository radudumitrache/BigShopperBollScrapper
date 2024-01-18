from lxml import html
import requests

# Define the URL of the web page you want to scrape
URL = ("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/?bltgh=hv-IEzy4P"
       "-OI9nskywJCaA.2_18.22.ProductTitle")
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


def extract_decimal_number(text):
    # Extract decimal numbers from a text
    try:
        # Remove currency symbols and whitespace
        clean_text = ''.join(filter(lambda x: x.isdigit() or x == ',' or x == '.', text.strip()))

        # Replace the comma with a dot if it's used as a decimal separator
        if ',' in clean_text:
            # Check if comma is used as thousands separator
            if clean_text.count(',') == 1 and clean_text.count('.') == 0:
                clean_text = clean_text.replace(',', '.')
            # If comma and dot both are present, assume comma is thousands separator and remove it
            elif '.' in clean_text:
                clean_text = clean_text.replace(',', '')
        # Convert to float
        decimal_number = float(clean_text)
        return decimal_number
    except ValueError:
        return None


def product_price(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        page_content = html.fromstring(response.content)

        # Extract current price
        price_elements = page_content.xpath('//span[contains(@class, "promo-price")]/text()')
        price = None
        if price_elements:
            price = extract_decimal_number(price_elements[0])

        # Extract old price
        old_price_elements = page_content.xpath('//span[contains(@class, "promo-price__discount-amount")]/text()')
        old_price = None
        if old_price_elements:
            old_price = extract_decimal_number(old_price_elements[0])

        # Extract shipping price if necessary
        # shipping_price_elements = page_content.xpath('XPATH_FOR_SHIPPING_PRICE')
        # shipping_price = None
        # if shipping_price_elements:
        #     shipping_price = extract_decimal_number(shipping_price_elements[0])

        return (price, old_price)  # , shipping_price if shipping price is included

    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


if __name__ == "__main__":
    result = product_price(URL)
    if result:
        price, old_price = result
        print(f"Price: {price}")
        print(f"Old Price: {old_price}" if old_price is not None else "Old Price: Not available")
        # print(f"Shipping Price: {shipping_price}" if shipping_price is not None else "Shipping Price: Not available")
    else:
        print("Failed to retrieve the price.")