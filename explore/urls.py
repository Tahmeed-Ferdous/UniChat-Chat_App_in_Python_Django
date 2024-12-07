# explore/urls.py
from django.urls import path
from . import views

app_name = 'explore'  # Ensure you have an app namespace

urlpatterns = [
    path('', views.explore_page, name='explore_page'),  # Maps to the explore page view
]
