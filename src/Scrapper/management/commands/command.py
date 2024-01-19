import json
import random

from django.core.management.base import BaseCommand

from .scrapper_functions import *

class Command(BaseCommand):
    help = "Scrape bol.com product information"

    def add_arguments(self, parser):
        parser.add_argument("--headless", action='store_true', help="Input the headless options")
        parser.add_argument("--search", help="Input the search query (ean or title)", nargs = '*', type=str, required=True)
        parser.add_argument("--region", help="Input the region NL/BE", nargs = '*', type=str, required=True)

    def handle(self, *args, **kwargs):
        headless = kwargs["headless"]
        search = kwargs["search"]
        region = kwargs["region"].pop().lower()

        if not ("nl" in region or "be" in region):
            print("Please enter a valid region")
            return

        with open("headers.json") as json_data:
            data = json.load(json_data)
            # select random header
            headers = random.choice(data)

        with open("xpath.json") as json_data:
            xpath = json.load(json_data)

        products_urls = searchForItem(search, headers, xpath["search"], region)

        for product_url in products_urls:
            product_info = get_product_info(product_url, headers, xpath["product_info"])
            all_sellers_info = get_all_sellers_info(product_url, headers, xpath["all_sellers_info"])
            country_code = get_country_code(product_url, headers)
            product_name = get_product_name(product_url, headers, xpath["product_name"])
            product_price = get_product_price(product_url, headers, xpath["product_price"])

            result_dict = {
                "name" : product_name,
                "product_price" : product_price,
                "country_code" : country_code,
                "product_info" : product_info,
                "other_sellers" : all_sellers_info,
            }
            print(result_dict)
            #save product to db

# Command to run
# python manage.py command --website=bol.com --search="your_search_query" --headless
