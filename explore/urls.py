from django.urls import path
from . import views

app_name = 'explore'

urlpatterns = [
    path('', views.explore_page, name='explore_page'),
]
