from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
def dashboard(request):
    return render(request, 'dashboard.html',locals())