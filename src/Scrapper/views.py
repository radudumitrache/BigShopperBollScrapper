from django.db.models import Case, When, Value, F, DecimalField
from django.shortcuts import render, redirect, reverse
from .models import ScraperConfig, Product, Price, ProductSpecification, Feeds, Partner, ProductPartner, ScraperConfig
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def display_data(request):
    scraper_configs = ScraperConfig.objects.all()
    products = Product.objects.prefetch_related(
        'price_set',  # Assuming Price has a reverse relation to Product
        'feeds_set',  # Assuming Feeds has a reverse relation to Product
        'productpartner_set',  # Assuming ProductPartner has a reverse relation to Product
    ).all()
    prices = Price.objects.all()

    # Preprocess prices
    for price in prices:
        if price.SalePrice == 0 and price.OriginalPrice != 0:
            price.display_sale_price = f'Identical ({price.OriginalPrice})'
        else:
            price.display_sale_price = price.SalePrice

    product_specifications = ProductSpecification.objects.all()
    feeds = Feeds.objects.all()
    partners = Partner.objects.all()
    product_partners = ProductPartner.objects.all()
    country_code = scraper_configs.first().country if scraper_configs.exists() else 'Not Defined'

    return render(request, 'display_data.html', {
        'scraper_configs': scraper_configs,
        'products': products,
        'prices': prices,
        'product_specifications': product_specifications,
        'feeds': feeds,
        'partners': partners,
        'product_partners': product_partners,
        'country_code': country_code,
    })


def search_product(request):
    return render(request, 'index_search.html')


@csrf_protect
def scrape_product(request):
    if request.method == 'POST':
        product_search = request.POST.get('product_search')
        if product_search:
            # Redirect to your scraping view with the product information
            return redirect('Scrapper:scrape_product_details', product_info=product_search)
    return redirect('Scrapper:scrape_product_details', product_info=product_search)


def scrape_product_details(request, product_info):
    try:
        # Call your scraping function (replace 'scrape_product_info' with your actual function)
        result_json = None
        if result_json:
            # Return the scraped data as an HTTP response
            return HttpResponse(result_json, content_type='application/json')
        else:
            # Handle the case when scraping fails
            return HttpResponse("Error: Unable to fetch product information.", status=500)
    except Exception as e:
        # Handle exceptions that may occur during scraping
        return HttpResponse(f"Error: {str(e)}", status=500)