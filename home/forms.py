from django import forms
from django.forms import ClearableFileInput
from crispy_forms.layout import Layout, HTML, Row, Column
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Project, Images, User, UserProfile
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from datetime import datetime
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Date modules
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


# class Meta:
#     widgets = {                          # Here
#         'phone': PhoneNumberPrefixWidget(initial='US'),
#     }




class ProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = '__all__'





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
		# fields = '__all__'
		fields = (
				'title',
				'keywords',
				'description',
				'stage',
				'category',
				'date_started',
				'date_ended',
				'video',
				'contributors',
			)
		widgets = {
	        'date_started': forms.TextInput(attrs={'type': 'date'}),
	        'date_ended': forms.TextInput(attrs={'type': 'date', 'max': datetime.now()}),
	        'images': ClearableFileInput(attrs={'multiple': True}),
    }
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			 Row(
				Column('title', css_class='form-group col-md-6 mb-0 ml-2'),
                Column('keywords', css_class='form-group col-md-5 mb-0 ml-4'),
              
			),
			 Row(
				Column(
					'description',
					css_class='max-w-s'
				),
			),
			Row(
				Column('stage', css_class='col-md-4'),
				Column('date_started', css_class='col-md-4 mx-2'),
				Column( 'date_ended', css_class='col-md-4')
			),
			Row(
				Column('category', css_class='overflow-y-scroll max-h-40 mb-2'),
			),
			Row(
				Column( 'video', css_class='col-md-6 ml-3 w-screen-2xl'),
				Column( 'contributors', css_class='ml-3 w-screen-2xl')
			),
)


class ImageForm(ProjectForm):
	images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	
	class Meta(ProjectForm.Meta):
		fields = ProjectForm.Meta.fields + ('images',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.helper = FormHelper()
		self.helper.form_tag = True
		self.helper.layout.extend(
			 [Row(
				Column('images', css_class='form-group col-md-6 mb-0 ml-2'),             
			),
			 Row(
				Submit('submit', 'Submit', css_class='col-md-5 float-right my-3')
			)]
		)


class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'staff_id')
		field_classes = {'username': UsernameField}


	
