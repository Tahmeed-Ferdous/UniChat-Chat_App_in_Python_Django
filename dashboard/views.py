from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from dashboard.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import random

def dashboard(request):
    error_message = None

    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST.get('name')
        task = request.POST.get('task')
        title = request.POST.get('title')
        img = request.FILES.get('img')

        # Handle to-do list form (name and task)
        if name and task and not title and not img:
            User.objects.create(name=name, task=task)
            return redirect('dashboard')

        # Handle card creation form (name, title, task, and img)
        elif name and title and task and img:
            if User.objects.filter(name=name).exists():
                error_message = "A user with this name already exists."
            else:
                User.objects.create(name=name, title=title, task=task, img=img)
                return redirect('dashboard')

    # Separate tasks and cards
    tasks = User.objects.exclude(name='', task='')  # Tasks without title and image
    cards = User.objects.exclude(title='', img='')  # Cards with title and image

    # Sort tasks for display
    def extract_last_two_digits(task_obj):
        try:
            return int(task_obj.task[-2:])
        except (ValueError, AttributeError):
            return float('inf')

    sorted_tasks = sorted(tasks, key=extract_last_two_digits)

    # Render the dashboard page
    return render(request, 'dashboard.html', {
        'tasks': sorted_tasks,
        'cards': cards,
        'error': error_message
    })



def delete_task(request, task_id):
    task = User.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard')

def edit_task(request, id):
    task = get_object_or_404(User, id=id)
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.task = request.POST.get('task')
        task.save()
        return redirect('dashboard')
    return render(request, 'edit.html', {'task': task})

from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def send_mail_req(request):
    templates = {
        'absent': "Dear {recipient_name},\n\nThis is to inform you about my absence from work.\n\nRegards,\n{sender_name}",
        'sick_leave': "Dear {recipient_name},\n\nI'm currently unwell and need sick leave.\n\nRegards,\n{sender_name}",
        'makeup_proposal': "Dear {recipient_name},\n\nHere’s a proposal for making up missed work.\n\nRegards,\n{sender_name}",
    }

    if request.method == 'POST':
        sender_email = request.POST.get('sender_email')
        recipient_email = request.POST.get('recipient_email') # No longer a select
        template_type = request.POST.get('template_type')

        if sender_email and recipient_email and template_type in templates:
            sender_name = sender_email.split('@')[0]
            recipient_name = recipient_email.split('@')[0]
            email_body = templates[template_type].format(recipient_name=recipient_name, sender_name=sender_name)
            email_subject = "Notification: " + template_type.replace('_', ' ').title()

            try:
                send_mail(
                    email_subject,
                    email_body,
                    sender_email,
                    [recipient_email],  # Still a list for send_mail
                    fail_silently=False,
                )
                messages.success(request, "Email sent successfully!")
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
        else:
            messages.error(request, "Invalid input. Please fill out the form correctly.")

    return render(request, 'dashboard.html') # No need to pass recipients
