# from django.contrib import admin
from django.urls import path , include
# from .views import  cart_json
from . import views
# from signup import views
from menu import views



from . import views
urlpatterns = [
      path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
        # path('story/<str:name>', views.story, name="story"),

    # path('story/<str:name>', views.story, name='menu'),  # URL for the "Our Story" page
        # path('cart.json', cart_json, name='cart_json'),

 path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation
    # path('deals/', views.deals, name='deals'),  # URL for the "Deals" page
    # Add URLs for other pages as needed
    


]