import json
import re

import requests
from lxml import html

def clean_text(text):
    text = text.replace("\n", " ")
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def web_request(url, headers):
    response = requests.get(url, headers)
    return response

def get_product_info(url, headers, xpath):
    response = web_request(url, headers)

    if response.status_code == 200:
        results = dict()
        tree = html.fromstring(response.content)
        specs = tree.xpath(xpath[0])

        for spec in specs:
            spec_title = spec.xpath(xpath[1])
            spec_value = spec.xpath(xpath[2])

            if spec_title and spec_value:
                results[spec_title[0].strip()] = clean_text(spec_value[0].text_content().strip())

        json_string = json.dumps(results, indent=4)
        return json_string
    else:
        print("Error: ", response.status_code)
        return None
