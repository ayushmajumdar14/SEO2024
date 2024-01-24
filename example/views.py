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
                }}
                h1, p {{
                    text-align: center;
                    margin-top: 30px;  /* Adjust the top margin as needed */
                }}
            </style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
        </head>
        <body>
            <h1>UC DAVIS DATA SCIENCE: SEO 2024 - AYUSH MAJUMDAR, AKSHAJ JOSHI</h1>
            <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
