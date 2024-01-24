# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
<head>
    <style>
        body {
            background: linear-gradient(to right, #000000, #6A00FF);
            color: white;
            font-family: 'Orbitron', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh; /* Ensure the body takes the full viewport height */
            margin: 0; /* Remove default body margin */
        }
        h1, p {
            text-align: center;
            margin-bottom: 20px; /* Add spacing between elements */
        }
    </style>
</head>
<body>
    <h1>{{ title }} - {{ current_time }}</h1>
    <p>WELCOME {% for member in members %}{{ member }}{% if not forloop.last %}, {% endif %}{% endfor %}</p>
</body>
</html>
    '''
    return HttpResponse(html)
