from django import forms
from .models import Project
from crispy_forms.layout import Layout, HTML, Row, Column
from crispy_forms.helper import FormHelper

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
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			 Row(
				Column('title', css_class='form-group col-md-6 mb-0'),
                Column('keywords', css_class='form-group col-md-6 mb-0 mx-3'),
              
			),
			 Row(
				Column(
					'description',
					css_class='col-md-8'
				),
			)
		)