from django.contrib import admin
from help.models import Help

# class ServiceAdmin(admin.ModelAdmin):
    # list_display=('image','title','subtitle','description')
admin.site.register(Help)
