from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfileSuggestion, Category, Notification

@login_required
def explore_page(request):
    # Fetch profile suggestions for the logged-in user
    profile_suggestions = ProfileSuggestion.objects.filter(suggestion_for=request.user)
    
    # Fetch all categories
    categories = Category.objects.all()
    
    # Fetch notifications for the logged-in user, ordered by timestamp (newest first)
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

    # Render the 'explore_page.html' with the required context
    return render(request, 'explore/explore_page.html', {
        'profile_suggestions': profile_suggestions,
        'categories': categories,
        'notifications': notifications
    })
