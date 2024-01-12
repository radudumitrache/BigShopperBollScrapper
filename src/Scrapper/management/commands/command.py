from django.core.management.base import BaseCommand
#import bol scraper module 
#import bol scraper function
#import save_to_db
#import new prices from sellers
from .scrapper_functions import *
import json
from .scrapper_functions import *
class Command(BaseCommand):
    help = "Scrape bol.com product information"

    def add_arguments(self, parser):
        parser.add_argument("--website", help="Input bol.com", type=str)
        parser.add_argument("--search", help="Input the search query (ean,title)", type=str)
        parser.add_argument("--headless", action='store_true', help="Input the headless options")

    def handle(self, *args, **kwargs):
        website = kwargs["website"]
        search = kwargs["search"]
        option = kwargs["headless"]
        # url = scrape_bol(search, website)  # Adjust line based on bol.com scraping logic
        
        # result = scrape_bol_com(url)  # Adjust line based on bol.com scraping logic
        # new_prices = get_new_prices_from_sellers(url, option)

        # save_product_info(result, url, new_prices)
        print(option)

        product_Info = product_info(website)
        all_sellers_info = get_all_sellers_info()
        country_code = get_country_code(website)
        product_name = get_product_name(website)
        _product_price = product_price(website)

        result_dict = {
            "name" : product_name,
            "product_price" : _product_price,
            "country_code" : country_code,
            "product_info" : product_Info,
            "other_sellers" : all_sellers_info,
        }

        print(result_dict)

# Command to run
# python manage.py command --website=bol.com --search="your_search_query" --headless
