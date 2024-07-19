"""
URL configuration for Restauranto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from signup import views
from aboutus import views
from menu import views
from chefs import views
from MenuItems.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('home.urls')),
    path('', include('signup.urls')),
    path('', include('aboutus.urls')),
    path('', include('menu.urls')),
    
    path('', include('chefs.urls')),
    path('', include('store.urls')),
    
    path('', include('deals.urls')),
    path('', include('contact.urls')),
    path('', include('help.urls')),
    path('', include('career.urls')),
    path('', include('story.urls')),
    path('', include('adminpanel.urls')),
    path('', include('MenuItems.urls')),
 path('MenuItems', home_page, name='fastfood'),
    path('cart/', cart_page, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_Item/', updateItem, name='update_Item'),
    path('dineIn/', dine_in, name='dineIn'),

    # path('', include('reservation.urls')),
        # path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation

    # path('login/', include('login.urls')), 
    # path('signup/', include('signup.urls')), 
        # path('signup/', views.signup_pg, name="signup"),
            # path('login/', views.login_pg, name="login"),

              path('', TemplateView.as_view(template_name='createpost.html'), name='createpost'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


