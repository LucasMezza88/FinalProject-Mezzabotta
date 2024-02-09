from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("unavailable/", unavailable, name="unavailable"),
]

