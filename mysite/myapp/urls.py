from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Maps root URL to the home view
]