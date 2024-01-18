from django.urls import path
from . import views
from .views import scrape_product

app_name = 'Scrapper'  # Add this line to set the app_name

urlpatterns = [
    path('display/', views.display_data, name='display_data'),
    path('search/', views.search_product, name='search_product'),
    path('scrape/', views.scrape_product, name='scrape_product'),  # Specify the full view path
    path('scrape_details/', views.scrape_product_details, name='scrape_product_details'),
]
