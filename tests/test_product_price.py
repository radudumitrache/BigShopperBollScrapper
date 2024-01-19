import json
import unittest

from src.Scrapper.management.commands.scrapper_functions import product_price

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

with open("src/xpath.json", "r") as f:
    xpath = json.load(f)
    print(xpath)

class TestProductPrice(unittest.TestCase):
    def test_get_product_price_testProductWithDiscount(self):
        result = product_price.get_product_price("https://www.bol.com/nl/nl/p/fast-1-10/9300000152080045/", headers, xpath["product_price"])
        self.assertTrue(type(result) is tuple)

    def test_get_product_price_testProductWithOnePrice(self):
        result = product_price.get_product_price("https://www.bol.com/nl/nl/p/qmusic-presesnts-het-beste-uit-de-top-40-2023-3/9300000162688764/", headers, xpath["product_price"])
        self.assertTrue(type(result) is float)

    def test_get_product_price_InvalidUrl(self):
        with self.assertRaises(expected_exception=Exception):
            product_price.get_product_price("https://Invalid", headers, xpath["product_price"])
