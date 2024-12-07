# explore/urls.py
from django.urls import path
from . import views

app_name = 'explore'  # Ensure that the app name is correctly set

urlpatterns = [
    path('', views.explore_page, name='explore_page'),  # This maps the URL '/explore/'
]
