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
                    margin-top: 15vh;
                }}
                p {{
                    margin-top: 5vh;
                    text-align: center;
                }}
                .custom-text-container {{
                    max-width: 80%;
                    margin: 20vh auto;  /* Bring the box down */
                    background: linear-gradient(to right, #6A00FF, #8E24AA);
                    padding: 20px;
                    border-radius: 8px;
                    position: relative;
                    height: 80vh;  /* Quadruple the height of the box */
                }}
                .custom-text, .bold-text {{
                    font-family: 'Poppins', sans-serif;
                    text-align: center;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    margin: 0;
                    max-width: 80%;  /* Fit the text within the box */
                }}
                .custom-text {{
                    font-size: 40px;
                    color: white;
                }}
                .bold-text {{
                    font-weight: bold;
                    font-size: 40px;
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
