from django.urls import path
from . import views

app_name = 'explore'

urlpatterns = [
    path('', views.explore_page, name='explore_page'),
    path('profile-suggestions/', views.profile_suggestions, name='profile_suggestions'),
    path('search/', views.search_posts, name='search_posts'),
    path('filter/<str:category>/', views.filter_posts, name='filter_posts'),
]
