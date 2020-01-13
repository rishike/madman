"""madman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import HomeView
# from rest_framework import routers
# from .api.serializer import UserViewSet
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="blog.home"),
    # path('', include(('accounts.urls'), namespace='accounts')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/', include(router.urls), name='api'),
    # path('api/profile/', include('user_profile.api.urls', namespace="profile-api")),
    # path('language/', include('languages.urls'),name='language'),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    path('map/', include('map.urls', namespace="map"))
]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))