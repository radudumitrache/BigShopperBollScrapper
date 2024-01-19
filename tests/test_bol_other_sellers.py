import json
import unittest

from src.Scrapper.management.commands.scrapper_functions.bol_other_sellers import get_all_sellers_info

url = "https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

with open("src/xpath.json", "r") as f:
    xpath = json.load(f)
    print(xpath)

class TestOtherSellers(unittest.TestCase):
    def test_is_dict(self):
        result = get_all_sellers_info(url, headers, xpath["all_sellers_info"])
        self.assertIs(type(result), dict)

    def test_invalid_url_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            result = get_all_sellers_info("Invalid", headers, xpath["all_sellers_info"])
            self.assertIsNotNone(result)
