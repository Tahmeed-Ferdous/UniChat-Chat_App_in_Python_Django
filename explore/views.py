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

    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT following_id FROM explore_follow WHERE follower_id = %s",
            [user.id]
        )
        following_profiles = cursor.fetchall()

    followed_user_ids = [row[0] for row in following_profiles]

    profile_suggestions = Profile.objects.filter(
        ~Q(user__in=followed_user_ids),
        ~Q(user=user),
        user__is_superuser=False
    )

    context = {
        'following_profiles': followed_user_ids,
        'profile_suggestions': profile_suggestions,
    }
    
    return render(request, 'explore/explore.html', context)


