from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from post.models import Post
from .models import Follow
from django.db.models import Q
from .models import Friend
from authy.models import Profile


@login_required
def explore_page(request):
    # Get users the logged-in user is following
    following_profiles = Follow.objects.filter(follower=request.user)
    followed_users = [friend.following for friend in following_profiles]  # Followed users are in `friend.following`

    # Get posts from the users the current user is following
    posts = Post.objects.filter(user__in=followed_users).order_by('-posted')

    # Profile suggestions: excluding users the current user is following
    followed_user_ids = [user.id for user in followed_users]  # Extract the IDs of followed users
    suggestions = User.objects.exclude(id__in=followed_user_ids)

    context = {
        'following_profiles': following_profiles,
        'posts': posts,
        'suggestions': suggestions,
    }
    
    return render(request, 'explore/explore.html', context)

@login_required
def profile_suggestions(request):
    # Profiles the current user is already following
    following_profiles = Follow.objects.filter(follower=request.user)
    following_ids = [f.following.id for f in following_profiles]

    # Exclude users the current user is following
    suggestion = User.objects.exclude(id__in=following_ids)

    # Fetch Profile data for suggestions
    suggestions = Profile.objects.filter(user__in=suggestion)

    context = {
        'suggestions': suggestions
    }
    return render(request, 'explore/profile_suggestions.html', context)


@login_required
def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(caption__icontains=query) | Q(tags__title__icontains=query)).distinct()
    else:
        posts = Post.objects.none()

    context = {
        'posts': posts
    }
    return render(request, 'explore/search_posts.html', context)

@login_required
def filter_posts(request, category):
    # Filter posts based on the selected category (e.g., 'Blockchain')
    posts = Post.objects.filter(tags__title__iexact=category)

    context = {
        'posts': posts,
        'category': category,  # Pass the category to the template
    }
    return render(request, 'explore/filter_posts.html', context)

