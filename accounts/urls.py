from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView



#scooter300
app_name = 'accounts'


urlpatterns = [
    path("login/", views.Login.as_view() , name="login" ),
    # path("signup", views.Signup.as_view(), name="signup"),
    # path("signup/post", views.Signup.as_view(), name="post")
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout")
  ]