import unittest

from src.Scrapper.management.commands.scrapper_functions.country_code import get_country_code

class TestCountryCode(unittest.TestCase):
    def test_expect_nl(self):
        result = get_country_code("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")
        self.assertEqual(result, "NL")

    def test_expect_be(self):
        result = get_country_code("https://www.bol.com/be/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/")
        self.assertEqual(result, "BE")

    def test_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            get_country_code("Invalid")
