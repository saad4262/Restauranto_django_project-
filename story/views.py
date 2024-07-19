from django.shortcuts import render,redirect
from chefs.models import ChefsModel
# Create your views here.

def index(request):
    return render(request, 'home.html')

def story(request):
        # chefsData=ChefsModel.objects.all()
        return render(request, "story.html")
  
def google_auth_view(request):
    return redirect("home")  

