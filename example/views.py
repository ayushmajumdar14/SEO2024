# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <head>
            <style>
                body {{
                    background: linear-gradient(to right, #000000, #6A00FF);
                    color: white;
                    font-family: 'Orbitron', sans-serif;
                    margin: 0;  /* Remove default body margin */
                    padding: 0; /* Remove default body padding */
                }}
                h1, p {{
                    text-align: center;
                    margin-top: 15vh;  /* 15% of the viewport height for title */
                }}
                p {{
                    margin-top: 5vh;  /* 5% of the viewport height for subtitle */
                }}
                nav {{
                    text-align: center;
                    margin-top: 2vh;  /* Adjust margin as needed */
                }}
                nav a {{
                    margin: 0 15px;
                    text-decoration: none;
                    color: #ffffff;
                    font-weight: bold;
                }}
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
    '''
    return HttpResponse(html)
