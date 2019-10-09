from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.views import View

from .forms import SignUpForm,RegisterForm,UserForm
from django.views.generic.edit import FormView,CreateView
from .models import Account
from user_profile.models import Profile
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Register(TemplateView):
	template_name = "accounts/register.html"

	def get(self, request):
		context_data = {'main':UserForm, 'secondary':RegisterForm}

		return render(request,self.template_name, context_data)
	

	def post(self, request):
		# form = Register(request.POST)
		loggedIn = False
		user_form = UserForm(data=request.POST)
		profile_form = RegisterForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			# data = form.cleaned_data
			username = user_form.cleaned_data['username']
			email = user_form.cleaned_data['email']
			password = user_form.cleaned_data['password']
			phone_number = profile_form.cleaned_data['phone_number']
			gender = profile_form.cleaned_data['gender']
			dob = profile_form.cleaned_data['dob']
			print(user_form.cleaned_data)
			print(profile_form.cleaned_data)

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save()
			profile.user = user
			profile.name = username
			profile.email = email
			profile.save()

			loggedIn = True

			
			return render(request,"accounts/complete.html", {'username':username, 'loggedIn':loggedIn})
		
		context_data = {'main':user_form, 'secondary':profile_form,
				'loggedIn':loggedIn
			}
		return render(request,self.template_name, context_data)





class Login(TemplateView):
	template_name="accounts/login.html"

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username, password)
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return render(request,"accounts/index.html", {'user':user})
		else:
			return HttpResponse("Input do not match")








# class Signup(FormView):
# 	"""docstring for Signup"""
# 	template_name="accounts/signup.html"
# 	form_class = SignUpForm
# 	model = Account
# 	# success_url = '/signup/post'

# 	# def form_valid(self, form):
# 	# 	# data = form.cleaned_data
# 	# 	# obj = self.model(**data)
# 	# 	# obj.save()
# 	# 	# form.save()
# 	# 	return super().form_valid(form)

# 	def post(self, request):
# 		form = SignUpForm(request.POST)
# 		context_data = {'form':form}
# 		if form.is_valid():
# 			data = form.cleaned_data
# 			self.model(**data).save()
# 			username = form.cleaned_data['username']
# 			return render(request,"accounts/complete.html", {'username':username})
		

# 		return render(request,self.template_name, context_data)





def logout_view(request):
	logout(request)
	return render(request, "accounts/index.html")	