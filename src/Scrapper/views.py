from django.shortcuts import render
from django.db import connection
from .models import Product


def index(request):
    # Retrieve all products
    products = Product.objects.all()
    print(products)  # Add this line to check if products are retrieved

    # Now, execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(str(products.query))
        print(cursor.fetchall())

    # Try querying a specific product by primary key
    try:
        product = Product.objects.get(pk=1)  # Assuming there's a product with ID 1
        print(product)
    except Product.DoesNotExist:
        print("Product with ID 1 does not exist")

    return render(request, 'index.html', {'products': products})
