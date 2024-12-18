from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone for datetime fields if needed
from post.models import Post  # Assuming Post model is in the post app

class ProfileSuggestion(models.Model):
    user = models.ForeignKey(User, related_name='explore_profile_suggestions', on_delete=models.CASCADE)
    suggestion_for = models.ForeignKey(User, related_name='explore_suggested_profiles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} suggests {self.suggestion_for.username}"

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='explore_notifications', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='explore_sent_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification from {self.sender.username} to {self.user.username}"

class Friend(models.Model):
    follower = models.ForeignKey(User, related_name='explore_friend_followers', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='explore_friend_followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='explore_follow_followers', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='explore_follow_following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
