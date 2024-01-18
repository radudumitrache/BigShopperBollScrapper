import unittest

from src.Scrapper.management.commands.scrapper_functions.search_for_product import searchForItem

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

class TestSearchForProduct(unittest.TestCase):
    def test_product_name_expect_success(self):
        result = searchForItem(["sony-official-playstation-5-dualsense-controller"], headers)
        self.assertEqual(result[0], "https://bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")

    def test_ean_expect_success(self):
        result = searchForItem(["0711719577171"], headers)
        self.assertEqual(result[0], "https://bol.com/nl/nl/p/playstation-5-disc-edition-slim/9300000166374057/")

    def test_mix_input_expect_success(self):
        result = searchForItem(["0711719577171", "sony-official-playstation-5-dualsense-controller"], headers)
        self.assertEqual(result[0], "https://bol.com/nl/nl/p/playstation-5-disc-edition-slim/9300000166374057/")
        self.assertEqual(result[1], "https://bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")

    def test_invalid_product_name_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            searchForItem("Invalid", headers)
