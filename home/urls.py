from django.contrib import admin
from django.urls import path , include
from .views import  cart_json
# from . import views
from signup import views


from aboutus import views
from . import views

# from .views import index, cart_json, my_view  # Import my_view from your views file

urlpatterns = [
    path('', views.index , name="home"),
    # path('', views.reservation1, name='home'),
   
    # path('login/', views.login_pg, name="login"),
    # path('signup/', views.signup_pg, name="signup"),
        # path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation
        # path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation

     path('cart.json', cart_json, name='cart_json'),
        #  path('aboutus/', views.aboutus , name="aboutus"),
        # path('my-view/', my_view, name="my_view"),

    #    path('signupletter/', views.signupletter, name='signupletter'),

    # path('login/', views.user_login, name='login'),
    # path('signup/', views.user_signup, name='signup'),
    # path('logout/', views.user_logout, name='logout'),
]
