from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import *


def index(request):
    return render(request, "core/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
