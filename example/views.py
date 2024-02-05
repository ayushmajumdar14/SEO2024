from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')


def project_leads(request):
     return render(request, 'project_leads.html')

def developers(request):
    return render(request, 'developers.html')

def team(request):
    return render(request, 'team.html')

def journey(request):
    return render(request, 'journey.html')
