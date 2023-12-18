from django.core.management.base import BaseCommand
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
