from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <div class="bg-black text-white min-h-screen flex flex-col items-center justify-center">
  <nav class="absolute top-0 left-0 right-0 flex justify-between items-center p-4 border-b border-purple-600">
    <div class="text-xl font-bold">ML/AI</div>
    <div class="flex space-x-4">
      <a class="hover:text-purple-500" href="#">
        About
      </a>
      <a class="hover:text-purple-500" href="#">
        Project Leads
      </a>
      <a class="hover:text-purple-500" href="#">
        Developers
      </a>
      <a class="hover:text-purple-500" href="#">
        Journey
      </a>
    </div>
  </nav>
  <header class="text-center mb-8">
    <h1 class="text-4xl font-bold mb-2">AI solution for Search Engine Optimization</h1>
    <p class="text-purple-300">WELCOME ANKITA, ANUNAY, ASISE, COREY, SARRAYU, TYLER, AND AIMEE</p>
  </header>
  <div class="bg-[#ffffff1a] backdrop-blur-sm text-white py-12 px-8 rounded-lg max-w-2xl">
    <blockquote class="text-2xl font-semibold text-purple-400">
      "We are a group of UC Davis students aiming to develop modern AI-powered solutions to improve your website's
      online presence."
    </blockquote>
  </div>
  <footer class="text-center mt-8 text-white">
    <p>
      Made with <span class="text-red-500">❤\u{fe0f}</span> by UC Davis Data Science Club
    </p>
  </footer>
</div>
    </html>
    '''

    


    
return HttpResponse(html)

def about(request):
    return HttpResponse("<h2>About Us Page</h2>")

def project_leads(request):
    return HttpResponse("<h2>Project Leads Page</h2>")

def developers(request):
    return HttpResponse("<h2>Developers Page</h2>")

def journey(request):
    return HttpResponse("<h2>Journey Page</h2>")
