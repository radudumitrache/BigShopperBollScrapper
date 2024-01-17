import requests
from lxml import html

def get_product_name(url_to_scrape):
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

        return name #,url_to_parse //ONLY if we want to return the url to be scraped

    else:
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")
