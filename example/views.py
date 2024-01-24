# example/views.py
from datetime import datetime
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def project_leads(request):
    return render(request, 'project_leads.html')

def developers(request):
    return render(request, 'developers.html')

def journey(request):
    return render(request, 'journey.html')

def index(request):
    now = datetime.now()
    return render(request, 'index.html', {'now': now})
# example/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project_leads/', views.project_leads, name='project_leads'),
    path('developers/', views.developers, name='developers'),
    path('journey/', views.journey, name='journey'),
]
<!-- templates/index.html -->
<html>
<head>
    <style>
        body {
            background: linear-gradient(to right, #000000, #6A00FF);
            color: white;
            font-family: 'Orbitron', sans-serif;
            margin: 0;
            padding: 0;
        }
        h1, p {
            text-align: center;
            margin-top: 15vh;
        }
        p {
            margin-top: 5vh;
        }
        nav {
            text-align: center;
            margin-top: 2vh;
        }
        nav a {
            margin: 0 15px;
            text-decoration: none;
            color: #ffffff;
            font-weight: bold;
        }
    </style>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
</head>
<body>
    <h1>UC DAVIS DATA SCIENCE: SEO 2024 - AYUSH MAJUMDAR, AKSHAJ JOSHI</h1>
    <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
    
    <nav>
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'project_leads' %}">Project Leads</a>
        <a href="{% url 'developers' %}">Developers</a>
        <a href="{% url 'journey' %}">Journey</a>
    </nav>
</body>
</html>
