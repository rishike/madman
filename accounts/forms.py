from django import forms
# from .formHelper import add_required_label_tag,cssclass_adder
from django.forms.forms import BoundField
# from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Account

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_profile.models import Profile

class RegisterForm(forms.ModelForm):

	class Meta:
		model=Profile
		fields=('phone_number', 'gender', 'dob')


	# name = forms.CharField(label='Name',min_length=3, max_length=30)
	phone_number = forms.CharField(label='Phone Number',min_length=3, max_length=14,required=False)
	gender = forms.ChoiceField(label='Gender',choices=[('', ''), 
			('m', 'Male'), ('fm', 'Female'),
			('ot', 'other')])
	dob = forms.DateField(label='Birth Date', input_formats=['%d/%m/%Y'],required=False)

	dob.widget.attrs.update({'class':'datepicker', 'id':'dob', 
						'placeholder': 'Your Birth Date or leave it blank'})


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField(label='Email', max_length=30)
	class Meta:
		model=User
		fields = ('username','password', 'email')


		

class SignUpForm(forms.Form):

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix','')
		super(SignUpForm, self).__init__(*args, **kwargs)


	class Meta:
		model = Account
		# fields = ['username', 'first_name', 'last_name', 'gender', 'password', 'email', 'dob']

	# BoundField.label_tag =  add_required_label_tag(BoundField.label_tag)

	username = forms.CharField(label='Username',min_length=3, max_length=30)
	first_name = forms.CharField(label='First Name',min_length=3, max_length=30,required=False)
	last_name = forms.CharField(label='Last Name',min_length=3, max_length=30,required=False)
	gender = forms.ChoiceField(label='Gender', required=False,choices=[('', ''), 
			('male', 'Male'), ('female', 'Female'), 
				('other', 'Other')],label_suffix='')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	email = forms.EmailField(label='Email', max_length=30)
	dob = forms.DateField(label='Birth Date', input_formats=['%d/%m/%Y'],required=False)

	username.widget.attrs.update({'id':'username', 'class':'validate', 
							'placeholder':'Username'})
	first_name.widget.attrs.update({'id':'first_name', 'class':'validate', 
							'placeholder':'First Name'})
	last_name.widget.attrs.update({'id':'last_name', 'class':'validate', 
								'placeholder':'Last Name or leave it blank'})
	gender.widget.attrs.update({'id':'gender'})
	password.widget.attrs.update({'id':'password', 'class':'validate',
			 'placeholder':'Fill Your Password'})
	email.widget.attrs.update({'id':'email', 'class':'validate', 'placeholder':'Email'})
	dob.widget.attrs.update({'class':'datepicker', 'id':'dob', 
						'placeholder': 'Your Birth Date or leave it blank'})



	# def clean(self):
	# 	username = self.cleaned_data.get('username')
	# 	first_name = self.cleaned_data.get('first_name')
	# 	last_name = self.cleaned_data.get('last_name')
	# 	gender = self.cleaned_data.get('gender')
	# 	password = self.cleaned_data.get('password')
	# 	email = self.cleaned_data.get('email')
	# 	birth_date = self.cleaned_data.get('birth_date')

	# 	# if username == "":
	# 	# 	self.add_error('username', 'Cannot be blank')
	# 		# raise forms.ValidationError("Username Cannot Be Blank")

	# 	return self.cleaned_data

	def clean_username(self):
		data = self.cleaned_data['username']
		if data == "":
			raise forms.ValidationError("Username Cannot Be Blank")
		elif Account.accountManager.filter(username=data):
			raise forms.ValidationError("Username already exist.")
		return data


	def clean_email(self):
		data = self.cleaned_data['email']
		if Account.accountManager.filter(email=data):
			raise forms.ValidationError("Email already exist.")
		return data



class LoginForm(forms.Form):
	username = forms.CharField(label='Username',min_length=3, max_length=30, required=False,label_suffix="")
	password = forms.CharField(label='Password', widget=forms.PasswordInput,label_suffix="")

