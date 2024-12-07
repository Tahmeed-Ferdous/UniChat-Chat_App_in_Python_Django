from django.db import models
from django.contrib.auth.models import User

# Profile Suggestions: Users that are not followed by the current user
class ProfileSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suggested_profiles')
    suggestion_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suggestions')

    class Meta:
        app_label = 'explore'

    def __str__(self):
        return f"Suggestion for {self.suggestion_for.username} by {self.user.username}"

# Categories for posts
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Notification model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
