
from django.contrib import admin
from menu.models import MenuModel 

class MenuAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description')  

admin.site.register(MenuModel, MenuAdmin) 
