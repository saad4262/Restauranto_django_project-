from django.shortcuts import render,redirect
from chefs.models import ChefsModel
from adminpanel.models import ChefModels
# Create your views here.

def index(request):
    return render(request, 'home.html')

def chefs(request):
        context={
             
        'ChefModels':ChefModels.objects.all()
        }
        return render(request, "chefs.html",  context)
  
def google_auth_view(request):
    return redirect("home")  

