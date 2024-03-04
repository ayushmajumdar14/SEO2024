from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .seoindustryscraper import crawl_website, google_search, extract_keywords_from_links




def index(request):
    return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def project_leads(request):
     return render(request, 'project_leads.html')

def developers(request):
    return render(request, 'developers.html')

def journey(request):
    return render(request, 'journey.html')

def team(request):
    return render(request, 'team.html')

def tool(request):
    return render(request, 'tool.html')


