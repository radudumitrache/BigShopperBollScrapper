import unittest

from src.Scrapper.management.commands.scrapper_functions.bol_other_sellers import get_all_sellers_info

class TestOtherSellers(unittest.TestCase):
    def test_is_dict(self):
        result = get_all_sellers_info("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")
        self.assertIs(type(result), dict)

    def test_is_not_none(self):
        result = get_all_sellers_info("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")
        self.assertIsNotNone(result)
