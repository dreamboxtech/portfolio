from django.urls import path
from .views import (
        home, about, contact, 
        projects, register_project,
        project_details, update_project,
        delete_image, delete_project,
        my_projects, Profile
    )


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
    path('register_project', register_project, name='reg_project'),
    path('projects/<int:pk>', project_details, name='project_details'),
    # path('<int:pk>/update_project', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/update_project', update_project, name='update_project'),
    path('projects/<int:pk>/delete_image', delete_image, name='delete_image'),
    path('projects/<int:pk>/delete_project', delete_project, name='delete_project'),
    path('profile', Profile.as_view(), name='.profile'),

    path('myprojects', my_projects, name='myprojects'),
]
