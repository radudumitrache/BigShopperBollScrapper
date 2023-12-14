import json

from django.core.management.base import BaseCommand
#import bol scraper module
#import bol scraper function
#import save_to_db
#import new prices from sellers
from .scrapper_functions import *
class Command(BaseCommand) :
    help = "Commands for presentation"
    def add_arguments(self, parser):
        parser.add_argument("url" , help = "Input the url of the product" , type = str)
    def handle(self, *args, **kwargs):
        url = kwargs["url"]
        product_Info = product_info(url)
        all_sellers_info = get_all_sellers_info(url)
        country_code = get_country_code(url)
        product_name = get_product_name(url)
        product_price = get_product_price(url)
        result_dict = {
            "name" : product_name ,
            "product_price" : product_price,
            "country_code" :country_code,
            "product_info" :product_Info,
            "other_sellers" : all_sellers_info,
        }
        with open("result.json","w") as outfile :
             json.dump(result_dict,outfile)
        self.stdout.write(f"The result has been saved in the file : \n\n\n {result_dict}")