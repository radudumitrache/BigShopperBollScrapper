from django.urls import path, include
from django.contrib import admin
from Scrapper.views import display_data  # Import the display_data view

app_name = 'Scrapper'
urlpatterns = [
    path('', display_data, name='home'),  # Use display_data as the root URL view
    path('admin/', admin.site.urls),
    path('myapp/', include('Scrapper.urls')),
    # Other URL patterns
]
