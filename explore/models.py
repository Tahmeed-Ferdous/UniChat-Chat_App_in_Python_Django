from django.db import models
from django.contrib.auth.models import User
from post.models import Post  # Assuming Post model is in post app

class ProfileSuggestion(models.Model):
    user = models.ForeignKey(User, related_name='suggestions', on_delete=models.CASCADE)
    suggestion_for = models.ForeignKey(User, related_name='suggested_profiles', on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    follower = models.ForeignKey(User, related_name='explore_following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='explore_followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
