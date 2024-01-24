from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <head>
            <style>
                /* Existing styling */
            </style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap">
        </head>
        <body>
            <header>
                <nav>
                    <a href="/about">About</a>
                    <a href="/project_leads">Project Leads</a>
                    <a href="/developers">Developers</a>
                    <a href="/journey">Journey</a>
                </nav>
            </header>
            <h1>ML/AI solution for Search Engine Optimization</h1>
            <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
            <div class="custom-text-container">
                <p class="custom-text">"We are a group of UC Davis students aiming to develop modern AI-powered solutions to improve your website's online presence."</p>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)

def about(request):
    return render(request, 'about.html')

def project_leads(request):
    return render(request, 'project_leads.html')

def developers(request):
    return render(request, 'developers.html')

def journey(request):
    return render(request, 'journey.html')
