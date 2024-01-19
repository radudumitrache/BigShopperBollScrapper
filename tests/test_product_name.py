import json
import unittest

from src.Scrapper.management.commands.scrapper_functions.product_name import get_product_name

url = "https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

with open("src/xpath.json", "r") as f:
    xpath = json.load(f)
    print(xpath)

class TestProductName(unittest.TestCase):
    def test_expect_success(self):
        result = get_product_name(url, headers, xpath["product_name"])
        self.assertEqual("Sony PlayStation DualSense draadloze controller - PS5", result)

    def test_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            get_product_name("Invalid", headers, xpath["product_name"])
