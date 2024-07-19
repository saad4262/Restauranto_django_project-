from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    #  path('auth/google/', views.google_auth_view, name='google_auth'),  # Adjust the view name as per your implementation
    #     path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs

    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('reset_password/', views.reset_password, name='reset_password'),
   
 path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]