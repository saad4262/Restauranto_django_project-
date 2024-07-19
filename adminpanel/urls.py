# from django.contrib import admin
from django.urls import path , include
# from .views import  cart_json
from . import views
# from signup import views



from . import views
urlpatterns = [
      path('', views.index, name='home'),
    path('adminpanel/', views.adminpanel, name="adminpanel"),
    path('adminLogin/', views.Admin_Login, name="Admin_Login"),
        # path('cart.json', cart_json, name='cart_json'),

 path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation

    path('logout/', views.user_logout, name='logout'),
            path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path("update/<str:id>", views.update, name="update"),
        path('delete/<int:id>/', views.delete_employee, name='delete'),

]