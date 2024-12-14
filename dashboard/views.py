from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from dashboard.models import User

def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        task = request.POST.get('task')
        if name and task:
            User.objects.create(name=name, task=task)
        return redirect('dashboard')
    
    tasks = User.objects.all()

    def extract_last_two_digits(task):
        try:
            return int(task.task[-2:])
        except ValueError:
            return float('inf')

    sorted_tasks = sorted(tasks, key=extract_last_two_digits)
    return render(request, 'dashboard.html', {'tasks': sorted_tasks})

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