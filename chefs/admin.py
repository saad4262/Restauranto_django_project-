from django.contrib import admin
from chefs.models import ChefsModel

# class ServiceAdmin(admin.ModelAdmin):
#     list_display=('image','name','title')
admin.site.register(ChefsModel)
