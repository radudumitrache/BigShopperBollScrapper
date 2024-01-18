from django.core.management.base import BaseCommand
from Scrapper.models import ScraperConfig, Product, Price, ProductSpecification, Feeds, Partner, ProductPartner
from django.utils import timezone
import json


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def add_arguments(self, parser):
        parser.add_argument('country_code', type=str, help='The country code to be used in ScraperConfig')

    def handle(self, *args, **kwargs):
        country_code = kwargs['country_code']

        # Create a new ScraperConfig instance with the provided country code
        scraper_config = ScraperConfig(
            config_settings='{"setting1": "value1", "setting2": "value2"}',
            country=country_code,  # Use the provided country code
            last_updated_timestamp=timezone.now(),
            version='1.0'
        )
        scraper_config.save()

        # Create a sample Product
        product = Product(
            scraper_config=scraper_config,
            ean='1234567890123',
            product_title='Sample Product Title',
            product_url='https://www.example.com/product',
            last_scraped_timestamp=timezone.now()
        )
        product.save()

        # Create a sample Price for the Product
        price = Price(
            ProductID=product,
            OriginalPrice=49.99,
            SalePrice=39.99,
            ShippingPrice=5.99,
            PriceTimestamp=timezone.now(),
            PriceDate=timezone.now().date()
        )
        price.save()

        # Create a sample ProductSpecification for the Product
        product_spec = ProductSpecification(
            ProductID=product,
            SpecificationTimestamp=timezone.now()
        )
        product_spec.save()

        # Create a sample Feed for the Product
        feed = Feeds(
            ProductID=product,
            FeedURL='https://www.example.com/feed',
            LastRetrievedTimestamp=timezone.now(),
            FeedType='XML',
            LastStatus='OK'
        )
        feed.save()

        # Create a sample Partner
        partner = Partner(
            Name='Sample Partner',
            IntegrationDetails=json.dumps({"key": "value"}),
            LastDataSentTimestamp=timezone.now()
        )
        partner.save()

        # Create a sample ProductPartner relationship
        product_partner = ProductPartner(
            ProductID=product,
            PartnerID=partner,
            IntegrationDetails=json.dumps({"key": "value"}),
            LastDataSentTimestamp=timezone.now()
        )
        product_partner.save()

        # Now you can access the 'id' attributes
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created and saved sample data in the database'))
