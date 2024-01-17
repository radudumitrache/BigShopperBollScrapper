import unittest

from src.Scrapper.management.commands.scrapper_functions.product_name import get_product_name

class TestProductName(unittest.TestCase):
    def test_expect_ps4(self):
        self.assertIn("controller", get_product_name("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"))

    def test_does_not_throw_error(self):
        self.assertIsNotNone(get_product_name("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"))
