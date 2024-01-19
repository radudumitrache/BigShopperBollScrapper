from django.urls import path,include
from . import views

urlpatterns = [
    path('display/', views.display_data, name='display_data'),
    path('search/', views.search_product, name='search_product'),
    path('scrape/', views.scrape_product, name='scrape_product'),  # Specify the full view path
    path('scrape_details/', views.scrape_product_details, name='scrape_product_details'),
]
