from django.contrib import admin
from django.urls import path
from Scrapper import views  # Import views from the Scrapper app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL pattern pointing to Scrapper's views.index
    # ... your other url patterns
]
