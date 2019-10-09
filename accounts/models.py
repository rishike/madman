from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver,Signal
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your models here.


# id username first name last name gender dob 
# mobile email nickname password type created_at updated_at
# deleted_at is_super_admin api_token

class Account(models.Model):

	class Meta:
		db_table= 'account'


	def __str__(self):
		return self.username

	accountManager = models.Manager()
	
	# username = models.CharField(max_length=30, unique=True)
	# first_name = models.CharField(max_length=30)
	# last_name = models.CharField(max_length=30)
	# gender = models.CharField(max_length=6)
	# dob = models.DateField(null=True)
	# email = models.EmailField(max_length=254, unique=True)
	# nickname = models.CharField(max_length=30, blank=True)
	# password = models.CharField(max_length=254)
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)
	# deleted_at = models.DateTimeField(null=True)
	# is_super_admin = models.BooleanField(default=False)
	# api_token = models.CharField(max_length=254, blank=True)





# @receiver(pre_save, sender=Account, )
# def preSaveCallback(sender, instance, **kwargs):
# 	# instance.validate_unique()
# 	instance.password = make_password(instance.password)	