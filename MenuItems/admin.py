from django.contrib import admin
from MenuItems.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'image', 'price', 'ingredients', 'product_description' )


class CartDataAdmin(admin.ModelAdmin):
    list_display = ('order','name','email','number', 'zipcode', 'address', 'city', 'province', 'instruction' )




admin.site.register(dineIn)
admin.site.register(shipping_address, CartDataAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
