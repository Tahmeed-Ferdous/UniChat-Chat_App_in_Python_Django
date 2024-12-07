from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ProfileSuggestion, Category, Notification

class ExploreTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.category = Category.objects.create(name='AI', description='Artificial Intelligence topics')

    def test_profile_suggestions(self):
        ProfileSuggestion.objects.create(user=self.other_user, suggestion_for=self.user)
        suggestions = ProfileSuggestion.objects.filter(suggestion_for=self.user)
        self.assertEqual(suggestions.count(), 1)

    def test_category_display(self):
        response = self.client.get(reverse('explore:explore_page'))  # Ensure 'explore:explore_page' is correct
        self.assertEqual(response.status_code, 200)  # Ensure response is 200
        self.assertContains(response, self.category.name)

    def test_notifications(self):
        Notification.objects.create(user=self.user, message='You have a new follower!')
        notifications = Notification.objects.filter(user=self.user)
        self.assertEqual(notifications.count(), 1)
