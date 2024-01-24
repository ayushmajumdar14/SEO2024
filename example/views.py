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
                    margin: 0;
                    padding: 0;
                }}
                h1 {{
                    text-align: center;
                    margin-top: 10vh;
                }}
                p {{
                    margin-top: 3vh;
                    text-align: center;
                }}
                .custom-text-container {{
                    max-width: 70%;
                    margin: 10vh auto;  /* Bring the box down */
                    background: linear-gradient(to right, #6A00FF, #8E24AA);
                    padding: 20px;
                    border-radius: 15px;  /* Rounded corners */
                    position: relative;
                }}
                .custom-text {{
                    font-family: 'Poppins', sans-serif;
                    text-align: center;
                    margin: 0;
                    font-size: 24px;
                    color: white;
                }}
            </style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap">
        </head>
        <body>
            <h1>ML/AI solution for Search Engine Optimization</h1>
            <p>WELCOME ANKITA, ANUNAY, ASISE, COREY, SARAYU, TYLER, AND AIMEE</p>
            <div class="custom-text-container">
                <p class="custom-text">"We are a group of UC Davis students aiming to develop modern AI-powered solutions to improve your website's online presence."</p>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)
