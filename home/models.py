from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	pass

class UserProfile(models.Model):
	user =  models.OneToOneField(User, on_delete=models.CASCADE)

class Project(models.Model):
	"""Project model"""

	STAGES = [
    ('STD', 'STARTED'),
    ('CMPT', 'COMPLETED'),
    ('ONG', 'ONGOING'),
	]

	CATEGORIES = [
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

	]

	title = models.CharField(max_length=50, blank=False)
	keywords = models.CharField(max_length=100, verbose_name="Tech Stack (Comma Separated)")
	description = RichTextField(verbose_name="Project Description", config_name='my_basic_config')
	stage = models.CharField(choices=STAGES, max_length=20)
	date_started = models.DateField()
	date_ended = models.DateField()
	
	category = MultiSelectField(choices=CATEGORIES, default='BACKEND',
							    verbose_name="Project Category")
	technology = models.CharField(max_length=30, null=True)


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
