from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import messages
from django.views.generic import ( 
			DeleteView, UpdateView,
			CreateView, DetailView,
			TemplateView
			)
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from .forms import ProjectForm, ImageForm, CustomUserCreationForm, ProfileForm
from .models import Project, Images, User, UserProfile
from datetime import datetime




# Create your views here.
def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'home/test.html')

def about(request):
	# return HttpResponse("Fast forward")
	return render(request, 'about.html')

# Profile

class ProfileUpdateView(LoginRequiredMixin, CreateView):
	model = UserProfile
	form_class = ProfileForm
	template_name = 'home/profile_update.html'
	success_url = '/profile-update'
	# extra_context={'users': YourModel.objects.all()} #Alternative approach to set context data


	# def get_form_kwargs(self):
	# 	"""
	# 	Add to form data, set user before form save
	# 	"""
	# 	kwargs = super(ProfileUpdateView, self).get_form_kwargs()
	# 	if kwargs['instance'] is None:
	# 		kwargs['instance'] = UserProfile()
	# 	kwargs['instance'].user = self.request.user
		
	# 	return kwargs

	def form_valid(self, form):
		"""
		control form before save
		"""
		# print("form is: ", form.cleaned_data)

		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.country = form.cleaned_data['country']
		obj.state = form.cleaned_data['state']
		obj.city = form.cleaned_data['city']

		return super(ProfileUpdateView, self).form_valid(form)

	def get_context_data(self):
		"""
			Set context data with this method
		"""
		context = super(ProfileUpdateView, self).get_context_data()
		context['profile'] = UserProfile.objects.filter(user__id=self.request.user.id)
		return context


	# Use this method to overide, validate and save form
	# def form_valid(self, form):
		"""
		control form before save
		"""
	#     obj = form.save(commit=False)
	#     obj.user = self.request.user
	#     return super(PlaceFormView, self).form_valid(form)
		

	# def get_success_url(self):
	# 	return reverse('homer:profile')
	

# def Profile(request):
	"""
		Use method-based view for profile
	"""
# 	user = User.objects.get(id=request.user.id)
# 	profile = UserProfile.objects.filter(user__id=request.user.id)
# 	form = ProfileForm()
	
# 	print()

	
# 	if request.method == 'POST':
# 		form = ProfileForm(request.POST or None, request.FILES or None)
		
# 		if form.is_valid():
# 			profile = form.save(commit=False)
# 			profile.user = user
# 			profile.save()
# 			return redirect('/myprojects')
# 		else:
# 			print("Form error: ", form.errors)
			
# 	context = {
# 		'user': user,
# 		'form': form,
# 		'profile': profile
# 	}
# 	return render(request, 'home/profile_update.html', context)


class ProfileView(DetailView):

	template_name = 'home/profile.html'
	model = UserProfile

	# An elegant way to get url parameter
	# @property
	# def username(self):
	# 	return self.kwargs['username']

	def get_object(self):
		return get_object_or_404(User, username=self.kwargs['username'])

	def get_context_data(self, **kwargs):

		self.username = self.kwargs['username'] #get url data

		context = super(ProfileView, self).get_context_data(**kwargs)
		context['profile'] = UserProfile.objects.get(user__username=self.username)
		context['user'] = User.objects.get(username=self.username)
		context['projects'] = Project.objects.filter(user__username=self.username)

		# query project table
		try:
			num_projects = Project.objects.filter(user__username=self.username).count()
		except:
			num_projects = 0
		context['num_projects'] = num_projects

		print("Current user projects: ", num_projects)

		return context









# Signup class
class SignupView(CreateView):
	template_name = 'registration/signup.html'
	form_class = CustomUserCreationForm

	def get(self, request, *args, **kwargs):
		# if Application.objects.filter(user=self.request.user).exists():
		if request.user.is_authenticated:
			return redirect('/projects') # ideally you'd use the url name here instead.
		return super().get(request, *args, **kwargs)

	def get_success_url(self):
		return reverse('login')

class Login(LoginView):
	template_name = 'registration/login.html'
	# form_class = CustomUserCreationForm

	def get(self, request, *args, **kwargs):
		# if Application.objects.filter(user=self.request.user).exists():
		if request.user.is_authenticated:
			return redirect('/projects') # ideally you'd use the url name here instead.
		return super().get(request, *args, **kwargs)

	def get_success_url(self):
		return reverse('home:projects')

def projects(request):
	projects = Project.objects.prefetch_related('images_set').all()

	paginator = Paginator(projects, 6) #
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	

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
	contributors = project.contributors.split(',')

	
	context = {
		'project': project,
		'categories': categories,
		'images': images,
		'keywords': keywords,
		'contributors': contributors
	}
	return render(request, 'home/project_details.html', context)

@login_required
def register_project(request):
	project_form = ProjectForm()
	form = ImageForm()

	if request.method == 'POST':
		form = ImageForm(request.POST or None, request.FILES or None)
		files = request.FILES.getlist('images')
		print("Checking User: ", request.user)
		if form.is_valid():

			title = form.cleaned_data['title']
			keywords = form.cleaned_data['keywords']
			description = form.cleaned_data['description']
			stage = form.cleaned_data['stage']
			date_started = form.cleaned_data['date_started']
			date_ended = form.cleaned_data['date_ended']
			category = 	form.cleaned_data['category']
			video = form.cleaned_data['video']
			contributors = form.cleaned_data['contributors']
			
			project = Project.objects.create(
							user=request.user,
							title=title,
							keywords=keywords,
							description=description,
							stage=stage,
							date_started=date_started,
							date_ended=date_ended,
							category=category,
							video=video,
							contributors=contributors
				)
			# send_mail(
   #          subject=f"{datetime.now()}: a Project Created",
   #          message="This is to inform you that a new project has just been created.",
   #          from_email="test@dreamboxtech.com",
   #          recipient_list=["bbbolaleye@gmail.com", "info@dreamboxtech.com"]
   #      	)
			if files:
				for f in files:
					if len(Images.objects.filter(project__id=project.id)) == 6:
						messages.info(request, "Project registered, but images cannot exceed 6")
						return redirect('/myprojects')
					Images.objects.create(project=project, images=f)
			messages.success(request, "A new project has been successfully created.")
			return redirect('/myprojects')
		
	context = {

		'form': form
		
	}
	return render(request, "home/reg_project.html", context)

#formset
def change_filename(instance, filename):
	fpath = pathlib.Path(filename)
	new_fname =  str(uuid.uuid1()) # uuid1 --> uuid + timestamps
	return f"images/{new_fname}{fpath.suffix}"	
	
@login_required
def update_project(request, pk):
	
	# image_query = Images.objects.prefetch_related('project').filter(project_id=pk)
	# p = Project.objects.prefetch_related('images_set')
	# m = Images.objects.filter(project_id=pk).values_list('images', flat=True)


	project = Project.objects.get(id=pk)
	project_instance = ProjectForm(instance= project)
	images_qset = Images.objects.filter(project_id=pk)

	files = request.FILES.getlist('images')
	print("Results: ", project.user, request.user)
	if project.user == request.user:
		if request.method == 'POST':

			form = ProjectForm(request.POST, instance=project)
			if form.is_valid():
				form.save()
				# send_mail(
	   #          subject="A Project Updated2",
	   #          message="This is to inform you that a new project has just been updated.",
	   #          from_email="test@dreamboxtech.com",
	   #          recipient_list=["bbbolaleye@gmail.com", "info@dreamboxtech.com"]
	   #      	)
				messages.success(request, "The project has been successfully updated.")
				# return redirect(f'/projects/{pk}')
				return redirect(reverse('home:project_details', kwargs={'pk':pk}))

			if files:
				for f in files:
					if len(Images.objects.filter(project_id=pk)) == 6:
						messages.info(request, "Images cannot be more than 6")
						return redirect(f'/projects/{pk}/update_project')
					Images.objects.create(project=project, images=f)
				messages.success(request, "The images have been successfully updated.")
				return redirect(reverse('home:update_project', kwargs={'pk': pk}))
	else:
		messages.warning(request, "You do not have the permission to do that")
		return redirect('/myprojects')

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
	return redirect(f'/projects/{pid}/update_project')


def delete_project(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()
	messages.success(request, "The project has been successfully deleted.")
	return redirect('/projects')


# Personalized project view
@login_required
def my_projects(request):

	projects = Project.objects.filter(user=request.user)

	paginator = Paginator(projects, 6) #
	page_number = request.GET.get('page')
	page_object = paginator.get_page(page_number)

	context = {
		'projects': projects,
		'page_object': page_object
	}

	return render(request, "home/myprojects.html", context)



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
