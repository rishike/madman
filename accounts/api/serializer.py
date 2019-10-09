from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	url = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'url'
		]

	
		

