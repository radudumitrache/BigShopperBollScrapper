from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This makes it the root URL pattern
    # ... other URL patterns if needed
]
