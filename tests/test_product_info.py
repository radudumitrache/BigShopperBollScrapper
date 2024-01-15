from unittest import TestCase

from src.Scrapper.management.commands.scrapper_functions import product_info

class Test(TestCase):
    def test_product_info_validUrl(self):
        result = product_info("https://www.bol.com/nl/nl/p/clever-esports-ps4-rapid-fire-remappable-paddle-controller/9200000097445920/")
        self.assertTrue(type(result) is str)

    def test_product_info_invalidUrl(self):
        with self.assertRaises(expected_exception=Exception):
            product_info("Invalid Url")
