from django.shortcuts import render,redirect
from menu.models import MenuModel

def menu(request):
        Menudata=MenuModel.objects.all()
        return render(request, "menu.html", {'Menudata': Menudata})


def google_auth_view(request):
    return redirect("home")  


def index(request):
    return render(request, 'home.html')