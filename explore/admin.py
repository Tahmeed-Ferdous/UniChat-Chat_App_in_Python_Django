from django.contrib import admin
from .models import ProfileSuggestion, Category, Notification

admin.site.register(ProfileSuggestion)
admin.site.register(Category)
admin.site.register(Notification)
