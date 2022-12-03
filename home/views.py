from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    # return HttpResponse("Fast forward")
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, 'home/projects.html', context)

def register_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if  form.is_valid():            
            form.save()
            return redirect('/projects')
        
    context = {
        'form': form
    }
    return render(request, "reg_project.html", context)



