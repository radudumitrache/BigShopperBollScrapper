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
        result_dict = get_product_result_dictionary(url)
        with open("result.json","w") as outfile :
             json.dump(result_dict,outfile)
        self.stdout.write(f"The result has been saved in the file : \n\n\n {result_dict}")