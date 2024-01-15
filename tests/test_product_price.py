from unittest import TestCase

from src.Scrapper.management.commands.scrapper_functions import product_price

class Test(TestCase):
    def test_get_product_price_testProductWithDiscount(self):
        result = product_price.get_product_price("https://www.bol.com/nl/nl/p/fast-1-10/9300000152080045/")
        self.assertTrue(type(result) is tuple)

    def test_get_product_price_testProductWithOnePrice(self):
        result = product_price.get_product_price("https://www.bol.com/nl/nl/p/qmusic-presesnts-het-beste-uit-de-top-40-2023-3/9300000162688764/")
        self.assertTrue(type(result) is float)

    def test_get_product_price_InvalidUrl(self):
        result = product_price.get_product_price("https://Invalid")
        self.assertIsNone(result)
