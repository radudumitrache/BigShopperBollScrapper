from urllib.parse import urlparse
from lxml import html
import requests

# Define the URL of the web page you want to scrape
URL = "https://www.bol.com/nl/nl/p/playstation-5-console-disc-edition/9300000004162282/"
headers = {
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


def get_product_name(url_to_scrape):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url_to_scrape)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            parsed_content = html.fromstring(response.content)

            # Specify XPath expressions for name and URL
            xpath_name = '//span[@class="u-mr--xs"]/text()'

            # Extract data using specified XPaths
            name = parsed_content.xpath(xpath_name)[0] if parsed_content.xpath(xpath_name) else "N/A"

            return name  # ,url_to_parse //ONLY if we want to return the url to be scraped

        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
