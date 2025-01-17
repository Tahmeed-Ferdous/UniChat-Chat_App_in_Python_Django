from django.urls import path
from dashboard.views import listing, delete_task,delete_taskr, edit_task, send_mail_req,add_course,displayOnSchedule

urlpatterns = [
    path('listing/', listing ,name='listing'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('delete_taskr/<int:task_id>/', delete_taskr, name='delete_taskr'),
    path('send_mail/', send_mail_req, name='send_mail'),
    path('add_course/',add_course,name='add_course'),
    path('schedule/', displayOnSchedule, name='display_schedule'),
]
