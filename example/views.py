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
        <a href="{% https://seo-2024.vercel.app/ %}">About</a>
        <a href="{% https://seo-2024.vercel.app/ %}">Project Leads</a>
        <a href="{% https://seo-2024.vercel.app/ %}">Developers</a>
        <a href="{% https://seo-2024.vercel.app/ %}">Journey</a>
    </nav>
</body>
</html>
