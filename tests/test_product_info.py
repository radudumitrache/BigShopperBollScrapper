import json
import unittest

from src.Scrapper.management.commands.scrapper_functions import get_product_info

url = "https://www.bol.com/nl/nl/p/clever-esports-ps4-rapid-fire-remappable-paddle-controller/9200000097445920/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

with open("src/xpath.json", "r") as f:
    xpath = json.load(f)
    print(xpath)

class TestProductInfo(unittest.TestCase):
    def test_product_info_validUrl(self):
        result = get_product_info(url, headers, xpath["product_info"])
        self.assertTrue(type(result) is str)

    def test_product_info_invalidUrl(self):
        with self.assertRaises(expected_exception=Exception):
            get_product_info("Invalid Url", headers, xpath["product_info"])
