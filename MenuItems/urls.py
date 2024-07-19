
from django.urls import path, include
from . import views
urlpatterns = [
    path('MenuItems/', views.home_page, name='MenuItems'),
    path('MenuItems/', views.updateItem, name='update_Item'),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('dineIn/', views.dine_in, name='dinein'),
    path('success/', views.success, name='success'), 
    path('checkout_success/', views.checkout_success, name='checkout_success'), 

]