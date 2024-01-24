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
            </style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
        </head>
        <body>
            <h1>ML/AI solution for Search Engine Optimization</h1>
            <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
