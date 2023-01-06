from django.urls import path
from App_logueo.views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    











]