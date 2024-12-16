from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ProfileSuggestion, Notification, Friend
from post.models import Post
from django.db.models import Q

@login_required
def explore_page(request):
    profile_suggestions = ProfileSuggestion.objects.filter(user=request.user)
    notifications = Notification.objects.filter(user=request.user)
    friends_following = Friend.objects.filter(follower=request.user)

    print("Profile Suggestions:", profile_suggestions) 
    print("Notifications:", notifications) 
    print("Friends Following:", friends_following)

    context = {
        'profile_suggestions': profile_suggestions,
        'notifications': notifications,
        'friends_following': friends_following,
    }
    return render(request, 'explore/explore.html', context)

@login_required
def profile_suggestions(request):
    suggestions = User.objects.exclude(id__in=[f.followed.id for f in Friend.objects.filter(follower=request.user)])
    context = {
        'suggestions': suggestions if suggestions else [],
        'no_suggestions': not suggestions.exists(),
    }
    return render(request, 'explore/profile_suggestions.html', context)

@login_required
def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(caption__icontains(query)) | Q(tags__title__icontains(query))
        ).distinct()
    else:
        posts = Post.objects.none()
    context = {
        'posts': posts,
    }
    return render(request, 'explore/search_posts.html', context)

@login_required
def filter_posts(request, category):
    posts = Post.objects.filter(tags__title__iexact=category)
    context = {
        'posts': posts,
    }
    return render(request, 'explore/filter_posts.html', context)
