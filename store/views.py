from django.shortcuts import render,redirect
from menu.models import MenuModel
from home.models import Email
from home.forms import EmailForm
from django.core.mail import send_mail
import os  

def store(request):
        subject = "Welcome to Restauranto's Newsletter - Stay Connected!"
        message = "Dear Customer, Thank you for signing up for Restauranto's newsletter! We're thrilled to have you join our community. By subscribing to our newsletter, you'll be the first to know about exciting updates, special offers, and exclusive deals available only to our subscribers. From mouthwatering new menu items to upcoming events and promotions, we'll keep you informed so you never miss out on the latest happenings at Restauranto. Stay connected with us and explore all that we have to offer. Whether you're craving your favorite dish or eager to discover something new, we're here to delight your taste buds and provide you with exceptional dining experiences. If you have any questions or feedback, please don't hesitate to reach out. We value your input and look forward to serving you soon!Best regards,The Restauranto's Team"
    
        form1 = EmailForm()
        if request.method == 'POST':
             form1 = EmailForm(request.POST)
             if form1.is_valid():
                recipient = form1.cleaned_data['recipient']
                send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [recipient])
                form1.save()
                return redirect('login')  # Redirect to email_sent view
        else:
            
            form1 = EmailForm()
        context={
             
        }
        # Menudata=MenuModel.objects.all()
        return render(request, "store.html",{'form1': form1})


def google_auth_view(request):
    return redirect("home")  


def index(request):
    return render(request, 'home.html')