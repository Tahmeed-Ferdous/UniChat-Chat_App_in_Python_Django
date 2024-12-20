from django.urls import path
from dashboard.views import dashboard, delete_task, edit_task, send_mail_req

urlpatterns = [
    path('dashboard/', dashboard ,name='dashboard'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('send_mail/', send_mail_req, name='send_mail'),
]
