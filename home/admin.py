# from django.contrib import admin
# from .models import Home

# class HomeAdmin(admin.ModelAdmin):
#     # pass
#     list_display = ('about_us',)  # Adjust this according to the fields in the Home model

# admin.site.register(Home, HomeAdmin)

# app1/admin.py

# from django.contrib import admin
# from home.models import Reservation

# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'city', 'num_people', 'date', 'message')

from django.contrib import admin
from home.models import Reservation

# class ReservationAdmin(admin.ModelAdmin):
#   list_display = ('name', 'phone_number','city', 'num_people', 'date', 'message')

admin.site.register(Reservation)


from django.contrib import admin
from .models import Email

# class EmailAdmin(admin.ModelAdmin):
#     list_display = ['recipient', 'subject', 'message']

admin.site.register(Email)
