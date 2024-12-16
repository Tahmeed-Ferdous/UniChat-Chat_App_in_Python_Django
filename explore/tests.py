from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ProfileSuggestion, Notification, Friend

class ExplorePageTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Create test data
        self.suggested_user = User.objects.create_user(username='suggested_user', password='password')
        self.notification_sender = User.objects.create_user(username='notification_sender', password='password')
        self.friend_user = User.objects.create_user(username='friend_user', password='password')

        ProfileSuggestion.objects.create(user=self.user, suggestion_for=self.suggested_user)
        Notification.objects.create(user=self.user, sender=self.notification_sender, message='Test notification')
        Friend.objects.create(follower=self.user, followed=self.friend_user)

    def test_explore_page_status_code(self):
        response = self.client.get(reverse('explore:explore_page'))
        self.assertEqual(response.status_code, 200)

    def test_explore_page_template(self):
        response = self.client.get(reverse('explore:explore_page'))
        self.assertTemplateUsed(response, 'explore/explore.html')

    def test_explore_page_context(self):
        response = self.client.get(reverse('explore:explore_page'))
        self.assertIn('profile_suggestions', response.context)
        self.assertIn('notifications', response.context)
        self.assertIn('friends_following', response.context)

    def test_profile_suggestions_content(self):
        response = self.client.get(reverse('explore:explore_page'))
        profile_suggestions = response.context['profile_suggestions']
        self.assertEqual(profile_suggestions.count(), 1)
        self.assertEqual(profile_suggestions.first().suggestion_for.username, 'suggested_user')

    def test_notifications_content(self):
        response = self.client.get(reverse('explore:explore_page'))
        notifications = response.context['notifications']
        self.assertEqual(notifications.count(), 1)
        self.assertEqual(notifications.first().message, 'Test notification')

    def test_friends_following_content(self):
        response = self.client.get(reverse('explore:explore_page'))
        friends_following = response.context['friends_following']
        self.assertEqual(friends_following.count(), 1)
        self.assertEqual(friends_following.first().followed.username, 'friend_user')
