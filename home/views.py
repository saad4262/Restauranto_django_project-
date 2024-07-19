# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Import messages module for displaying messages
from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Import messages module for displaying messages
# from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from allauth.socialaccount.models import SocialApp
# from django.core.exceptions import MultipleObjectsReturned
# from .models import Home  # Import the Home model
from aboutus.models import AboutUs
from menu.models import MenuModel
# from chefs.models import ChefsModel
from adminpanel.models import ChefModels

# from django.shortcuts import render, HttpResponse
# from .forms import ReservationForm
from django.shortcuts import render, redirect,HttpResponse
from .forms import ReservationForm

from django.core.mail import EmailMessage, get_connection
from django.conf import settings

from .forms import EmailForm
from .models import Email
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os  
from signup.forms import SignupForm
# def index(request):
#     # Assuming you want to fetch all instances of Home model
#     if Home.objects.exists():
#       AboutUsdata = Home.objects.all()
#       return render(request, 'home.html', {'AboutUsdata': AboutUsdata})
#     else:
#           print("error")
# # Create your views here.

# def homePage(request):
#         AboutUsdata=AboutUs.objects.all()
#         return render(request,"home.html", {'AboutUsdata': AboutUsdata})


from django.shortcuts import render
# from aboutus.models import AboutUs
from home.models import Reservation
# from signupletter.models import Email






def index(request):
    
    subject = "Welcome to Restauranto's Newsletter - Stay Connected!"
    message = "Dear Customer, Thank you for signing up for Restauranto's newsletter! We're thrilled to have you join our community. By subscribing to our newsletter, you'll be the first to know about exciting updates, special offers, and exclusive deals available only to our subscribers. From mouthwatering new menu items to upcoming events and promotions, we'll keep you informed so you never miss out on the latest happenings at Restauranto. Stay connected with us and explore all that we have to offer. Whether you're craving your favorite dish or eager to discover something new, we're here to delight your taste buds and provide you with exceptional dining experiences. If you have any questions or feedback, please don't hesitate to reach out. We value your input and look forward to serving you soon!Best regards,The Restauranto's Team"
    form = ReservationForm()
    form1 = EmailForm()
    
    if request.method == 'POST':
        # if 'reservation_submit' in request.POST:
            form = ReservationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  # Redirect to success page after saving
        # if 'signup_submit' in request.POST:
            form1 = EmailForm(request.POST)
            if form1.is_valid():
                recipient = form1.cleaned_data['recipient']
                send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [recipient])
                form1.save()
                return redirect('login')  # Redirect to email_sent view
    else:
            form = ReservationForm()
            form1 = EmailForm()

    context = {
        'about_us_data': AboutUs.objects.all(),
        'form': form,
        'form1': form1,
        'Menudata': MenuModel.objects.all(),
        'ChefModels': ChefModels.objects.all(),
        'signupletterData': Email.objects.all(),
        # 'SignupForm': SignupForm.objects.all()
    }
    return render(request, "home.html", context)




# def index(request):
  
#   if request.method == 'POST':
#     form = ReservationForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('login')  # Redirect to success page after saving
#   else:
#     form = ReservationForm()
#   context = {'about_us_data': AboutUs.objects.all(), 'form': form, "Menudata" :MenuModel.objects.all(), "chefsData":ChefsModel.objects.all(),"signupletterData" : Email.objects.all()}
#   return render(request, "home.html", context)


# def signupletter(request):
#     subject = "Texting Mail"
#     message = "This is a test mail"
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             recipient = form.cleaned_data['recipient']
#             # subject = form.cleaned_data['subject']
#             # message = form.cleaned_data['message']

#             send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [recipient])

#             return redirect('login')  # Redirect to email_sent view
#     else:
#         form = EmailForm()
#     return render(request, 'signupletter.html', {'form': form})





def cart_json(request):

    cart_data = {
        'item1': {'name': 'Product 1', 'quantity': 2, 'price': 10.99},
        'item2': {'name': 'Product 2', 'quantity': 1, 'price': 5.99},
    
    }
    return JsonResponse(cart_data)


def aboutus(request):
        return render(request, 'aboutus.html')



def login_pg(request):
        return render(request, 'login.html')
def signup_pg(request):
        return render(request, 'signup.html')




def logoutPage(request):
     logout(request)
     request.session.flush() 
     return redirect("login")

def google_auth_view(request):
    return redirect("home")  

def aboutus(request):
        AboutUsdata=AboutUs.objects.all()
        return render(request, "aboutus.html", {'AboutUsdata': AboutUsdata})
  



