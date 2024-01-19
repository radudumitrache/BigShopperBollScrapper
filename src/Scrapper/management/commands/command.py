import decimal
import datetime
from django.core.management.base import BaseCommand
#import bol scraper module 
#import bol scraper function
#import save_to_db
#import new prices from sellers
from .scrapper_functions import *
import json
import random
from django.utils import timezone
from django.core.management.base import BaseCommand
import re
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
        scraper_config = ScraperConfig.objects.filter(country="NL").first()
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
            product_price_values = get_product_price(product_url, headers)
            seller_name = "retrieve failed"

            if all_sellers_info is not None:
                for seller in all_sellers_info:
                    seller_info = all_sellers_info[seller]
                    if "seller_name" in seller_info:
                        seller_name = seller_info["seller_name"]
                        break  # Break the loop as soon as the seller name is found

                if seller_name:
                    # Split the full seller name into parts
                    name_parts = seller_name.split(' - ')
                    seller_name = name_parts[0]  # Save the desired part of the name

                    # Try to get an existing Partner with the same name or create a new one
                    partner, created = Partner.objects.get_or_create(
                        Name=seller_name,
                        defaults={'IntegrationDetails': json.dumps({})} , # Assuming IntegrationDetails is a JSON field
                        LastDataSentTimestamp= timezone.now()
                    )
                    partner.save()

                    if created:
                        print(f"New partner created: {seller_name}")
                    else:
                        print(f"Existing partner updated: {seller_name}")
                else:
                    print("Seller name is empty or not found.")
            else:
                print("Failed to retrieve seller's information.")

            result_dict = {
                "name" : product_name,
                "product_price" : product_price_values,
                "country_code" : country_code,
                "product_info" : product_info,
                "other_sellers" : all_sellers_info,
            }

            #try to find if the product already exists

            print(result_dict)

            #save product to db
            print(f"Seller Name: {seller_name}")

            # Check if the seller_name is not "retrieve failed"
            if seller_name != "retrieve failed":
                # Try to get an existing Partner with the same name or create a new one
                partner, created = Partner.objects.get_or_create(
                    Name=seller_name,
                    defaults={'IntegrationDetails': json.dumps({})}  # Assuming IntegrationDetails is a JSON field
                )

                # Update the LastDataSentTimestamp for the partner
                partner.LastDataSentTimestamp = timezone.now()
                partner.save()

                # Print for debugging
                if created:
                    print(f"New partner created: {seller_name}")
                else:
                    print(f"Existing partner updated: {seller_name}")

            try:
                # Use regular expressions to extract EAN from product_Info assuming it's a string
                ean_match = re.search(r'"EAN":\s*"(\d{13})"', product_info)
                if ean_match:
                    ean = ean_match.group(1)
                    print(f"Extracted EAN: {ean}")  # Debug print
                else:
                    print("Invalid or missing EAN, setting to default value.")
                    ean = "0000000000000"
            except Exception as e:
                print(f"Error while extracting EAN: {e}")  # Debug print
                ean = "0000000000000"

                # Use the 'description' variable when setting the 'details' field
            product = Product(
                scraper_config=scraper_config,
                ean=ean,
                product_title=product_name,
                product_url=product_url,
                last_scraped_timestamp=timezone.now(),
             # Use 'description' here, but limit it to 1000 characters
            )

            # Save the product instance before saving the price instance
            product.save()

            # Add this print statement to check the details field after setting it
            print(f"Details after setting details: {product.details}")

            if isinstance(product_price_values, tuple) and len(product_price_values) == 2:
                sale_price, original_price = product_price_values
            else:
                sale_price, original_price = product_price_values, product_price_values

            # Handle the case when original_price is None (set it to 0.0)
            if original_price is None:
                original_price = decimal.Decimal('0.0')

            # Save the actual prices in the database
            original_price_in_db = original_price
            sale_price_in_db = sale_price

            # If sale_price and original_price are the same, set display_sale_price to "identical"
            display_sale_price = "identical" if sale_price == original_price else sale_price

            # Print the values for confirmation
            print(f"Sale Price for Display: {display_sale_price}")
            print(f"Original Price: {original_price}")

            # Add print statements to check the values
            print(f"Sale Price: {sale_price}")
            print(f"Original Price: {original_price}")

            # Handle the case when original_price is None (set it to 0.0)
            if original_price is None:
                original_price = decimal.Decimal('0.0')

            # Create and save a Price instance with separate OriginalPrice and SalePrice
            price = Price(
                ProductID=product,
                OriginalPrice=original_price,  # Use the extracted original price or 0.0 if None
                SalePrice=sale_price,  # Use the extracted sale price
                ShippingPrice='0.00',  # Assign the extracted shipping price
                PriceTimestamp=timezone.now(),
                PriceDate=timezone.now().date()
            )
            price.save()

            # Create and save a ProductSpecification instance
            product_spec_info = {}  # Replace with the actual product specification data
            product_spec = ProductSpecification(ProductID=product, SpecificationTimestamp=timezone.now())
            product_spec.save()

            # Create and save a Feeds instance
            feed_info = {}  # Replace with the actual feed data
            feed = Feeds(ProductID=product, FeedURL=product_url, LastRetrievedTimestamp=timezone.now(),
                         FeedType='Product Updates', LastStatus='OK')
            feed.save()

            # Create and save a Partner instance with the retrieved seller name
            partner = Partner(Name=seller_name, IntegrationDetails={}, LastDataSentTimestamp=timezone.now())
            partner.save()

            # Create and save a ProductPartners instance with the retrieved seller name
            product_partner_info = {}  # Replace with the actual product-partner data
            product_partner = ProductPartner(ProductID=product, PartnerID=partner, IntegrationDetails={},
                                             LastDataSentTimestamp=timezone.now())
            product_partner.save()

            print(result_dict)
# Command to run
# python manage.py command --website=bol.com --search="your_search_query" --headless
