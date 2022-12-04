from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):


	# title = forms.CharField()
	# keywords = forms.CharField()
	# description = forms.CharField()
	# stage = forms.CharField()
	# date_started = forms.DateField()
	# date_ended = forms.DateField()
	# images = forms.ImageField()
	
	class Meta:
		model = Project
		fields = (
				'title',
				'keywords',
				'description',
				'stage',
				'date_started',
				'date_ended',
				'images',
			)
