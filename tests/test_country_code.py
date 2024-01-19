import unittest

from src.Scrapper.management.commands.scrapper_functions.country_code import get_country_code

url_nl = "https://www.bol.com/nl/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"
url_be = "https://www.bol.com/be/nl/p/sony-official-playstation-5-dualsense-controller/9300000007897748/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

class TestCountryCode(unittest.TestCase):
    def test_expect_nl(self):
        result = get_country_code(url_nl, headers)
        self.assertEqual(result, "NL")

    def test_expect_be(self):
        result = get_country_code(url_be, headers)
        self.assertEqual(result, "BE")

    def test_expect_exception(self):
        with self.assertRaises(expected_exception=Exception):
            get_country_code("Invalid", headers)
