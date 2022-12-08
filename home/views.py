from django.shortcuts import render, HttpResponse, redirect
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from .forms import ProjectForm, ImageForm
from .models import Project, Images

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
	images = Images.objects.all()

	paginator = Paginator(projects, 6) #
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)


	context = {
		'projects': projects,
		'page_obj': page_obj,
		'images': images
	}
	return render(request, 'home/projects.html', context)

def project_details(request, pk):

	# project = Project.objects.filter(id=pk)
	project = Project.objects.get(id=pk)

	images = Images.objects.filter(project__id=pk)
	keywords = project.keywords.split(',')
	categories = list(project.category)

	print(keywords)
	
	context = {
		'project': project,
		'categories': categories,
		'images': images,
		'keywords': keywords
	}
	return render(request, 'home/project_details.html', context)


def register_project(request):
	form = ImageForm()
	
	if request.method == 'POST':
		form = ImageForm(request.POST or None, request.FILES or None)
		files = request.FILES.getlist('images')
		
		if form.is_valid():
			title = form.cleaned_data['title']
			keywords = form.cleaned_data['keywords']
			description = form.cleaned_data['description']
			stage = form.cleaned_data['stage']
			date_started = form.cleaned_data['date_started']
			date_ended = form.cleaned_data['date_ended']
			category = 	form.cleaned_data['category']
			
			project = Project.objects.create(
							title=title,
							keywords=keywords,
							description=description,
							stage=stage,
							date_started=date_started,
							date_ended=date_ended,
							category=category
				)
				
			for f in files:
				Images.objects.create(project=project, images=f)
			
			return redirect('/projects')
		
	context = {
		'form': form,
		
	}
	return render(request, "home/reg_project.html", context)



def handler404(request, exception):
	return render(request, '404.html')
