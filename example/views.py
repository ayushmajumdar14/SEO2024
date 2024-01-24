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
                    font-family: 'Rajdhani', sans-serif;
                }}
                h1, p {{
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <h1>UC DAVIS DATA SCIENCE: SEO 2024 - AYUSH MAJUMDAR, AKSHAJ JOSHI</h1>
            <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
