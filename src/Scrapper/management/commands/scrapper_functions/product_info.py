import json
import re

import requests
from lxml import etree
from lxml import html

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
