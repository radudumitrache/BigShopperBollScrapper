import unittest

from src.Scrapper.management.commands.scrapper_functions.countryCode import get_country_code

class TestCountryCode(unittest.TestCase):
    def test_expect_nl(self):
        self.assertEqual(get_country_code("https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"), "NL")

    def test_expect_be(self):
        self.assertEqual(get_country_code("https://www.bol.com/nl/be/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"),"BE")
