from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
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

	paginator = Paginator(projects, 6) #

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'projects': projects,
		'page_obj': page_obj
	}
	return render(request, 'home/projects.html', context)

def project_details(request, pk):

	# project = Project.objects.filter(id=pk)
	project = Project.objects.get(id=pk)
	categories = list(project.category)
	print(categories)
	context = {
		'project': project,
		'categories': categories
	}
	return render(request, 'home/project_details.html', context)



def register_project(request):
	form = ProjectForm()
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		files = request.FILES.getlist('images')
		print("The files are: ", files)
		if  form.is_valid():
			for file in files:
				file_instance = Project(images=file)
				file_instance.save()            
			form.save()
			return redirect('/projects')
		
	context = {
		'form': form,
	}
	return render(request, "home/reg_project.html", context)



def handler404(request, exception):
	return render(request, '404.html')
