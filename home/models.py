from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField
from django_countries.fields import CountryField
from datetime import datetime, date
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
	staff_id = models.CharField(max_length=8, verbose_name="Staff ID", blank=True)
	first_name = models.CharField(max_length=20, verbose_name="First Name")
	middle_name = models.CharField(max_length=20, verbose_name="Middle Name")
	last_name = models.CharField(max_length=20, verbose_name="Last Name")
	dob = models.DateField(blank=True, default=date.today, verbose_name="Date of Birth")


class UserProfile(models.Model):
	
	user =  models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=1, choices=(('M','M'),('F','F')), verbose_name='Gender')
	photo = models.ImageField(upload_to='profile_pictures/', blank=True, verbose_name="Profile Picture")
	cover_photo = models.ImageField(upload_to='profile_pictures/', blank=True, verbose_name="Profile Picture")
	country = CountryField(blank_label='(select country)')
	about = RichTextField(max_length=500, verbose_name="About Me", config_name='another_config')
	address = models.CharField(max_length=150, blank=True, verbose_name="Address", default="None")
	phone = PhoneNumberField(null=False, blank=False, unique=True)
	job_title = models.CharField(max_length=100, verbose_name="Job title", help_text="Data Engineer")
	experience_years = models.IntegerField(max_length=2, verbose_name="Years of Experience")

	def __str__(self):
		return self.user.username

class Education(models.Model):
	EDUCATION_LIST = (
		("High School", "High School"),
		("Diploma", "Diploma"),
		("Associate", "Associate"),
		("Bachelors", "Bachelors"),
		("Masters", "Masters"),
		("PhD", "PhD"),
		("Others", "Others"),
		("None", "None"),
		)
	user =  models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	degree = models.CharField(max_length=50, choices=EDUCATION_LIST,verbose_name="Degree")
	course = models.CharField(max_length=100, blank=True, verbose_name="Course Studied")
	school = models.CharField(max_length=150, blank=True, verbose_name="Institution")
	grade = models.CharField(max_length=15, blank=True, verbose_name="Grade")
	year = models.DateField(blank=True, verbose_name="Year of Graduation")

class Work(models.Model):
	user =  models.ForeignKey(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=50, verbose_name="Job Title")
	organization = models.CharField(max_length=200, verbose_name="Oranization")
	specific_duties = RichTextField(verbose_name="Specific Duties", config_name='my_basic_config')
	work_started = models.DateField(blank=True, verbose_name="Dated Started")
	work_ended = models.DateField(blank=True, verbose_name="Date Ended")

class Social(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	facebook = models.URLField(max_length=150, blank=True, verbose_name="Facebook", default="None")
	twiiter = models.URLField(max_length=150, blank=True, verbose_name="Twitter", default="None")
	linkedin = models.URLField(max_length=150, blank=True, verbose_name="LinkedIn", default="None")
	stackoverflow = models.URLField(max_length=150, blank=True, verbose_name="Stackoverflow", default="None")


class Publications(models.Model):
	user =  models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150, blank=True, verbose_name="Publication Title")
	date = models.DateField(blank=True, verbose_name="Publication Date")
	link = models.URLField(max_length=200, blank=True, verbose_name="Publication Link")


class Project(models.Model):
	"""Project model"""

	STAGES = (
    ('STD', 'STARTED'),
    ('CMPT', 'COMPLETED'),
    ('ONG', 'ONGOING'),
	)

	CATEGORIES = (
		('MACHINE LEARNING', 'MACHINE LEARNING'),
		('DATA SCIENCE', 'DATA SCIENCE'),
		('DATA ANALYTICS/ANALYSIS', 'DATA ANALYTICS/ANALYSIS'),
		('BACKEND', 'BACKEND'),
		('FRONTEND', 'FRONTEND'),
		('MOBILE', 'MOBILE'),
		('DATA BASE', 'DATA BASE'),
		('BLOCKCHAIN', 'BLOCKCHAIN'),
		('CLOUD COMPUTING', 'CLOUD COMPUTING'),
		('COMPUTER NETWORKING', 'COMPUTER NETWORKING'),
		('SCRIPTING', 'SCRIPTING'),
		('DESKTOP', 'DESKTOP'),
		('SOFTWARE DEVELOPMENT', 'SOFTWARE DEVELOPMENT'),
		('GAME DEVELOPMENT', 'GAME DEVELOPMENT')

	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, blank=False)
	slug = AutoSlugField(max_length=200, populate_from='title', unique_with='id')
	keywords = models.CharField(max_length=100, verbose_name="Tech Stack (Comma Separated)")
	description = RichTextField(verbose_name="Project Description", config_name='my_basic_config')
	stage = models.CharField(choices=STAGES, max_length=20)
	date_started = models.DateField()
	date_ended = models.DateField()
	
	category = MultiSelectField(choices=CATEGORIES, verbose_name="Project Category", 
		max_length=100)
	technology = models.CharField(max_length=30, null=True)
	video = EmbedVideoField(verbose_name="Video Link", blank=True)
	contributors = models.CharField(max_length=200, blank=True, verbose_name="Contributors (Comma separated)")


	def __str__(self):
		return self.title


class Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True, null=True,
							   verbose_name="Project Images")

    def __str__(self):
    	# return self.project.title
    	return self.images.url





# Category, Technologies
