from django.db import models

# Create your models here.

class Project(models.Model):
	"""Project model"""

	STAGES = [
    ('STD', 'STARTED'),
    ('CMPT', 'COMPLETED'),
    ('ONG', 'ONGOING'),
	]

	title = models.CharField(max_length=50, blank=False)
	keywords = models.CharField(max_length=100)
	description = models.TextField(verbose_name="Project Description")
	stage = models.CharField(choices=STAGES, max_length=20)
	date_started = models.DateField(blank=False)
	date_ended = models.DateField()
	images = models.ImageField(upload_to='images/', blank=True, null=True)


	def __str__(self):
		return self.title

# Category, Technologies