from django.shortcuts import render,redirect
from chefs.models import ChefsModel
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

  
def google_auth_view(request):
    return redirect("home")  

