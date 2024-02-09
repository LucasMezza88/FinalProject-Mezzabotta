from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import *
from .models import *


def index(request):
    return render(request, "producto/index.html")

class ProductoCategoriaList(ListView):
    model = ProductoCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = ProductoCategoria.objects.all()
        return object_list

class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
