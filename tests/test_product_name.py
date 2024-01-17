import unittest

from src.Scrapper.management.commands.scrapper_functions.product_name import get_product_name

class TestProductName(unittest.TestCase):
    def test_expect_success(self):
        result = get_product_name("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")
        self.assertEqual("Sony PlayStation DualSense draadloze controller - PS5", result)

    def test_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            get_product_name("Invalid")
