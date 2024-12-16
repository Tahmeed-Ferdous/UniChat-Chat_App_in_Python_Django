from django.contrib import admin
from .models import ProfileSuggestion, Notification, Friend

admin.site.register(ProfileSuggestion)
admin.site.register(Notification)
admin.site.register(Friend)
