from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from notifications.models import Notification
# Create your views here.

def ShowNOtifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE notifications_notification SET is_seen = TRUE WHERE user_id = %s AND is_seen = FALSE",
            [user.id]
        )

    template = loader.get_template('notifications.html')

    context = {
        'notifications': notifications,
    }

    return HttpResponse(template.render(context, request))


def DeleteNotification(request, noti_id):
    user = request.user
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM notifications_notification WHERE id = %s AND user_id = %s", 
            [noti_id, user.id]
        )
    return redirect('show-notifications')


def CountNotifications(request):
    count_notifications = 0
    if request.user.is_authenticated:
        from django.db import connection
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM notifications_notification WHERE user_id = %s AND is_seen = FALSE",
                [request.user.id]
            )
            count_notifications = cursor.fetchone()[0]

    return {'count_notifications': count_notifications}
