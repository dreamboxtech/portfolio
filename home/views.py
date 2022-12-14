from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView

from django.core.paginator import Paginator
from .forms import ProjectForm, ImageForm #UpdateImageForm
from .models import Project, Images
from itertools import chain


# Create your views here.
def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def about(request):
	# return HttpResponse("Fast forward")
	return render(request, 'about.html')

def projects(request):
	projects = Project.objects.prefetch_related('images_set').all()
	# images = Images.objects.all()

	paginator = Paginator(projects, 6) #
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	# for project in projects:
	# 	print(project)
	

	context = {
		'projects': projects,
		'page_obj': page_obj,
	}
	return render(request, 'home/projects.html', context)

def project_details(request, pk):

	# project = Project.objects.filter(id=pk)
	project = Project.objects.get(id=pk)

	images = Images.objects.filter(project__id=pk)
	keywords = project.keywords.split(',')
	categories = list(project.category)

	
	context = {
		'project': project,
		'categories': categories,
		'images': images,
		'keywords': keywords
	}
	return render(request, 'home/project_details.html', context)


def register_project(request):
	project_form = ProjectForm()
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
			messages.success(request, "A new project has been successfully created.")
			return redirect('/projects')
		
	context = {

		'form': form
		
	}
	return render(request, "home/reg_project.html", context)

#formset
def change_filename(instance, filename):
	fpath = pathlib.Path(filename)
	new_fname =  str(uuid.uuid1()) # uuid1 --> uuid + timestamps
	return f"images/{new_fname}{fpath.suffix}"	
	

def update_project(request, pk):
	
	# image_query = Images.objects.prefetch_related('project').filter(project_id=pk)
	# p = Project.objects.prefetch_related('images_set')
	# m = Images.objects.filter(project_id=pk).values_list('images', flat=True)

	
	project = Project.objects.get(id=pk)
	project_instance = ProjectForm(instance= project)
	images_qset = Images.objects.filter(project_id=pk)

	files = request.FILES.getlist('images')
	
	
	if request.method == 'POST':

		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
			messages.success(request, "The project has been successfully updated.")
			return redirect(f'/projects/{pk}')


		if files:
			for f in files:
				if len(Images.objects.filter(project_id=pk)) == 6:
					return redirect(f'/{pk}/update_project')
				Images.objects.create(project=project, images=f)
			messages.success(request, "The images have been successfully updated.")
			return redirect(f'/{pk}/update_project')

	context = {
		'project': project_instance,
		'images': images_qset

	}

	

	return render(request, 'home/update_project.html', context)


def delete_image(request, pk):
	image = Images.objects.get(id=pk)
	pid = image.project_id
	image.delete()
	messages.info(request, "An image was deleted.")
	return redirect(f'/{pid}/update_project')


def delete_project(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()
	messages.success(request, "The project has been successfully deleted.")
	return redirect('/projects')





# class ProjectUpdateView(UpdateView, pk):
#     template_name = "home/update_project.html"
#     queryset = Images.objects.get(id=pk)
#     form_class = ImageForm

#     def get_success_url(self) -> str:
#         return reverse("homer:projects")


# class ProjectDeleteView(DeleteView):
#     template_name = "lead_delete.html"
#     queryset = Lead.objects.all()

#     def get_success_url(self) -> str:
#         return reverse("leader:home")


















def handler404(request, exception):
	return render(request, '404.html')
