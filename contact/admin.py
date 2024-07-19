from django.contrib import admin
from contact.models import Contact

# class ServiceAdmin(admin.ModelAdmin):
    # list_display=('image','title','subtitle','description')
admin.site.register(Contact)
