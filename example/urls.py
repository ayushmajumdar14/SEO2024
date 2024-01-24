from django.urls import path
from . import views
from example.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project_leads/', views.project_leads, name='project_leads'),
    path('developers/', views.developers, name='developers'),
    path('journey/', views.journey, name='journey'),
]
