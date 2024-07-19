from django.shortcuts import render,redirect
from .forms import HelpForm
# Create your views here.


def index(request):
    return render(request, 'home.html')

def help(request):
      if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
      else:
        form = HelpForm()     
      return render(request, "help.html")
  
def google_auth_view(request):
    return redirect("home")  

