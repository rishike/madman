from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

def imageUpload(instance, filename):
	return settings.STATICFILES_DIRS[0]+"\\img\\profile\\{filename}".format(filename=filename)


class Address(models.Model):
	street_address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pincode = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.city



class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True)
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=254, unique=True)
	phone_number = models.CharField(max_length=14, unique=True)
	gender = models.CharField(max_length=2, choices=[('m','male'),('fm','female'), ('ot','other')])
	profile_pic = models.ImageField(upload_to=imageUpload, blank=True, null=True)
	dob = models.DateField(null=True)
	permanent_address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="permanent_address", verbose_name="permanent address", null=True)
	company_address = models.OneToOneField(Address,on_delete=models.CASCADE, related_name="company_address", verbose_name="company address", null=True)
	friends = models.ManyToManyField("self", blank=True)

	def __str__(self):
		return self.name

	



