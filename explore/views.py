from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from post.models import Post
from .models import Follow
from authy.models import Profile

from django.db.models import Q

@login_required
def explore(request):
    user = request.user

    following_profiles = Follow.objects.filter(follower=user)
    followed_users = [friend.following for friend in following_profiles] 

    followed_user_ids = [user.id for user in followed_users]
    profile_suggestions = Profile.objects.filter(
        ~Q(user__in=followed_user_ids),
        ~Q(user=user),
        user__is_superuser=False
    )

    context = {
        'following_profiles': followed_users,
        'profile_suggestions': profile_suggestions,
    }
    
    return render(request, 'explore/explore.html', context)

