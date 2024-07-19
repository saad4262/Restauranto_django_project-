from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, ResetPasswordForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.models import User


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages  # Import messages module for displaying messages
# from django.http import JsonResponse
# from django.shortcuts import render, redirect,HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages  # Import messages module for displaying messages
# from django.contrib.auth import get_user_model
# # from django.shortcuts import redirect
# from allauth.socialaccount.models import SocialApp
# from django.core.exceptions import MultipleObjectsReturned


# Create your views here.
# Home page
def index(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('home')



def google_auth_view(request):
    return redirect("home")  

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.conf import settings
import os  # For using environment variables (optional)
from django.shortcuts import render
from .forms import ResetPasswordForm  # Ensure you have imported your form
from django.contrib.auth import get_user_model
from django.utils.html import format_html

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_user_model().objects.filter(email=email).first()
            if user:
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_link = f"http://127.0.0.1:8000/reset/{uid}/{token}/"  # Use your domain here
                email_address = os.environ.get('EMAIL_HOST_USER', 'your_default_email@example.com')
                # Pass the username to the email template
                email_content = render_to_string('email/password_reset_email.html', {'reset_link': reset_link, 'username': user.username})
                send_mail(
                    'Password Reset',
                    email_content,
                    email_address,
                    [email],
                    fail_silently=False,
                )
                return render(request, 'registration/password_reset_done.html')
    else:
        form = ResetPasswordForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})