from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfileSuggestion, Category, Notification

@login_required
def explore_page(request):
    profile_suggestions = ProfileSuggestion.objects.filter(suggestion_for=request.user)
    categories = Category.objects.all()
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'explore/explore_page.html', {
        'profile_suggestions': profile_suggestions,
        'categories': categories,
        'notifications': notifications
    })
