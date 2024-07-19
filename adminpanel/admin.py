# admin.py
from django.contrib import admin
from .models import ChefModels
from .models import AdminProfile




admin.site.register(ChefModels)
admin.site.register(AdminProfile)


