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
                    animation: backgroundAnimation 5s linear infinite; /* Animation properties */
                }}
                header {{
                    background: linear-gradient(to right, #333333, #000000);
                    padding: 10px 0;
                    border-bottom: 5px solid #6A00FF; /* Thick border at the bottom */
                    text-align: center;
                }}
                nav {{
                    display: flex;
                    justify-content: center;
                    padding: 10px 0;
                }}
                nav a {{
                    color: white;
                    text-decoration: none;
                    font-family: 'Poppins', sans-serif;
                    font-size: 18px;
                    font-weight: bold;
                    margin: 0 15px; /* Adjust the spacing between elements */
                    transition: color 0.3s;
                }}
                nav a:hover {{
                    color: #6A00FF; /* Change text color on hover */
                }}
                h1 {{
                    text-align: center;
                    margin-top: 5vh;
                }}
                p {{
                    margin-top: 3vh;
                    text-align: center;
                }}
                .custom-text-container {{
                    max-width: 60%;
                    margin: 20vh auto;  /* Bring the box down */
                    background: linear-gradient(to right, #6A00FF, #8E24AA);
                    padding: 20px;
                    border-radius: 15px;  /* Rounded corners */
                    position: relative;
                    height: 30vh;  /* Increase the overall height */
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }}
                .custom-text {{
                    font-family: 'Poppins', sans-serif;
                    text-align: center;
                    margin: 0;
                    font-size: 40px;
                    color: white;
                }}
                @keyframes backgroundAnimation {{
                    from {{
                        background-position: 0% 0%;
                    }}
                    to {{
                        background-position: 100% 100%;
                    }}
                }}
            </style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap">
        </head>
        <body>
            <header>
                <nav>
                    <a href="#about">About</a>
                    <a href="#project_leads">Project Leads</a>
                    <a href="#developers">Developers</a>
                    <a href="#journey">Journey</a>
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
