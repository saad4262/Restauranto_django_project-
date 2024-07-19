from django.contrib import admin
from aboutus.models import AboutUs

# class ServiceAdmin(admin.ModelAdmin):
    # list_display=('image','title','subtitle','description')
admin.site.register(AboutUs)


