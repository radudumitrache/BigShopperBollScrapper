import unittest

from src.Scrapper.management.commands.scrapper_functions.bol_other_sellers import get_all_sellers_info

url = "https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

class TestOtherSellers(unittest.TestCase):
    def test_is_dict(self):
        result = get_all_sellers_info(url, headers)
        self.assertIs(type(result), dict)

    def test_is_not_none(self):
        result = get_all_sellers_info(url, headers)
        self.assertIsNotNone(result)
