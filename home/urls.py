from django.urls import path
from .views import home, about, contact, projects, register_project


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
    path('register_project', register_project, name='reg_project')
]
