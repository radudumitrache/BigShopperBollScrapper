from urllib.parse import urlparse

import requests

def get_country_code(url_to_scrape, headers):
    # Send an HTTP request to the URL
    response = requests.get(url_to_scrape, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # split url by '/' and get second element for country code
        parsed_url = urlparse(url_to_scrape)
        path_components = parsed_url.path.split('/')

        # Check the country code based on the path
        if len(path_components) > 2:
            if path_components[1] == "nl":
                country_code = "NL"
            elif path_components[1] == "be":
                country_code = "BE"
            else:
                country_code = "N/A"
        else:
            country_code = "N/A"

        return country_code
    else:
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")
