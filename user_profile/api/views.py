from rest_framework import generics
from django.db.models import Q

from .serializer import ProfileSerializer

from user_profile.models import Profile
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions,viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import request



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

		
		
class ProfileCreateAPIView(generics.CreateAPIView):
	"""docstring for ProfileCreateAPIView"""
	serializer_class = ProfileSerializer




		
