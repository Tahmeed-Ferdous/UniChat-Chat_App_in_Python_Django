from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
def dashboard(request):
    for i in range(10):
        print("TEST TEST TEST TEST TEST TEST TEST")
    return render(request, 'dashboard.html',locals())