from django.urls import path
from . import views
from example.views import index


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('journey/', views.journey, name='journey'),
    path('tool/', views.tool, name='tool'),
    path('scrape/', views.scrape, name='scrape'),
]
