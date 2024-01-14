import unittest

from src.Scrapper.management.commands.scrapper_functions.search_for_product import searchForItem

class TestSearchProduct(unittest.TestCase):
    def test_search_ps5(self):
        self.assertIsNotNone(searchForItem(["playstation 5 controller"]))
