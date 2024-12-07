from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfileSuggestion, Category, Notification
from django.db.models import Prefetch

@login_required
def explore_page(request):
    # Fetch profile suggestions for the logged-in user, including related profile data to reduce queries
    profile_suggestions = ProfileSuggestion.objects.filter(suggestion_for=request.user).select_related('profile')

    # If 'profile' is a ForeignKey or OneToOne field, select_related is fine
    # If 'profile' is many-to-many or reverse ForeignKey, use prefetch_related instead
    
    # Fetch all categories (consider adding filters or pagination for performance if needed)
    categories = Category.objects.all()

    # Fetch notifications for the logged-in user, ordered by timestamp (newest first),
    # using select_related for the 'sender' (assuming sender is a ForeignKey or OneToOne relationship)
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp').select_related('sender')

    # Render the 'explore_page.html' with the required context
    return render(request, 'explore/explore_page.html', {
        'profile_suggestions': profile_suggestions,
        'categories': categories,
        'notifications': notifications
    })
