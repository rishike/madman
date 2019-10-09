from django.urls import path,include
from django.views.generic.base import RedirectView
from .views import ProfileViewSet
from rest_framework import routers

app_name = 'user_profile_api'


router = routers.DefaultRouter()
router.register(r'', ProfileViewSet)


urlpatterns = [
	path('',include(router.urls),name='profile')
]