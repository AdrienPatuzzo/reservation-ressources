from django.contrib import admin
from .models import Category, Location, Resource

# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Resource)