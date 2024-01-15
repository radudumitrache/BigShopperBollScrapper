from django.core.management.base import BaseCommand
#import bol scraper module 
#import bol scraper function
#import save_to_db
#import new prices from sellers
from .scrapper_functions import *
import json

from .scrapper_functions import *
from .scrapper_functions import search_for_product

class Command(BaseCommand):
    help = "Scrape bol.com product information"

    def add_arguments(self, parser):
        parser.add_argument("--website", help="Input bol.com", type=str)
        parser.add_argument("--headless", action='store_true', help="Input the headless options")
        parser.add_argument("--search", help="Input the search query (ean or title)", nargs = '*', type=str)
    def save_to_db(self, result : dict  ):
        pass
    def handle(self, *args, **kwargs):
        website = kwargs["website"]
        search = kwargs["search"]
        option = kwargs["headless"]
        # url = scrape_bol(search, website)  # Adjust line based on bol.com scraping logic
        
        # result = scrape_bol_com(url)  # Adjust line based on bol.com scraping logic
        # new_prices = get_new_prices_from_sellers(url, option)

        # save_product_info(result, url, new_prices)
        print(option)
        products_urls = search_for_product.searchForItem(search)
        for product_url in products_urls :
            product_Info = product_info(product_url)
            all_sellers_info = get_all_sellers_info(product_url)
            country_code = get_country_code(product_url)
            product_name = get_product_name(product_url)
            product_price = get_product_price(product_url)

            result_dict = {
                "name" : product_name,
                "product_price" : product_price,
                "country_code" : country_code,
                "product_info" : product_Info,
                "other_sellers" : all_sellers_info,
            }
            #try to find if the product already exists
            print(result_dict)
            #save product to db

# Command to run
# python manage.py command --website=bol.com --search="your_search_query" --headless
