import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BigShopper.settings')
django.setup()

from Scrapper.models import Product


def insert_product_data():
    # Define the product data
    product_data = [
        {
            'partnerid': 1,
            'ean': '1234567890123',
            'producttitle': 'Demostration purpose for video demonstration ',
            'producturl': 'https://example.com/product1',
            'sellername': 'Rares',
            'lastscrapedtimestamp': '2023-12-13 14:00:00+00:00',
        },
        {
            'partnerid': 2,
            'ean': '2345678901234',
            'producttitle': 'Demostration purpose for video demonstration ',
            'producturl': 'https://example.com/product2',
            'sellername': 'Seller 2',
            'lastscrapedtimestamp': '2023-12-13 15:00:00+00:00',
        },
    ]

    # Insert data into the Product table
    for data in product_data:
        Product.objects.create(**data)


if __name__ == "__main__":
    insert_product_data()
