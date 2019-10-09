from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from django.urls import reverse_lazy


class UserSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']

	# def get_url(self,obj):
	# 	return reverse_lazy("user-detail",kwargs={"username":obj.username})

   

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

