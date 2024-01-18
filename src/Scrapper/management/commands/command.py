
from django.core.management.base import BaseCommand
#import bol scraper module 
#import bol scraper function
#import save_to_db
#import new prices from sellers

from .scrapper_functions import *

import json
import random

from django.core.management.base import BaseCommand

from .scrapper_functions import *

from .scrapper_functions import search_for_product
import sys
from ...models import *
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

        products_urls = searchForItem(search, headers, region)

        for product_url in products_urls:
            product_info = get_product_info(product_url, headers)
            all_sellers_info = get_all_sellers_info(product_url, headers)
            country_code = get_country_code(product_url)
            product_name = get_product_name(product_url)
            product_price = get_product_price(product_url, headers)

            result_dict = {
                "name" : product_name,
                "product_price" : product_price,
                "country_code" : country_code,
                "product_info" : product_info,
                "other_sellers" : all_sellers_info,
            }

            #try to find if the product already exists

            print(result_dict)

            #save product to db

# Command to run
# python manage.py command --website=bol.com --search="your_search_query" --headless
