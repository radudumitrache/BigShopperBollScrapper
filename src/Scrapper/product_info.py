import json

import requests
from bs4 import BeautifulSoup

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
        soup = BeautifulSoup(response.content, 'lxml')
        specs = soup.find_all('div', class_='specs')
        for spec in specs:
            spec_list = spec.find('dl', class_='specs__list')
            if spec_list is None:
                continue
            spec_rows = spec_list.find_all('div', class_='specs__row')
            if spec_rows is None:
                continue
            for spec_row in spec_rows:
                spec_title = spec_row.find('dt', class_='specs__title').stripped_strings.__next__()
                spec_value = spec_row.find('dd', class_='specs__value').stripped_strings.__next__()
                if spec_title and spec_value:
                    results[spec_title] = spec_value
        json_string = json.dumps(results, indent=4)
        return json_string
    else:
        print("Error: ", response.status_code)
        return None

if __name__ == "__main__":
    results = product_info("")
    print(results)
    # might need to decode the json string as it does not support utf-8
    #text = bytes(text, encoding="raw_unicode_escape").decode('unicode_escape')
