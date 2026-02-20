from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ResourceListView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = "resources/resource_list.html"
    context_object_name = "resources"