from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
# Create your models here.

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
	keywords = models.CharField(max_length=100)
	description = RichTextField(verbose_name="Project Description", config_name='my_basic_config')
	stage = models.CharField(choices=STAGES, max_length=20)
	date_started = models.DateField(blank=False)
	date_ended = models.DateField()
	images = models.ImageField(upload_to='images/', blank=True, null=True)
	category = MultiSelectField(choices=CATEGORIES, default='BACKEND')
	technology = models.CharField(max_length=30, null=True)


	def __str__(self):
		return self.title

# Category, Technologies