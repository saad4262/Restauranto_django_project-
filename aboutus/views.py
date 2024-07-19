from django.shortcuts import render,redirect, get_object_or_404
from aboutus.models import AboutUs
# Create your views here.
# from menu.models import MenuModel
# from menu import views



def index(request):
    return render(request, 'home.html')

def aboutus(request):
        AboutUsdata=AboutUs.objects.all()
        # AboutUsdata = get_object_or_404(AboutUs, id=item_id)

        return render(request, "aboutus.html", {'AboutUsdata': AboutUsdata})

# from menu.models import MenuModel

# def story(request):
#         Menudata=AboutUs.objects.get(name=name)
#         if name == "Our Story":
#            return render(request, 'contact.html')
#         elif name == "Master Chefs":
#             return render(request, 'menu.html', {'Menudata':Menudata})
#         else:
#              return render(request,"signup.html")
        # return render(request, "menu.html", {'Menudata': Menudata})

  # views.py

# from django.shortcuts import render, get_object_or_404
# from .models import Item

# def item_detail(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     return render(request, 'item_detail.html', {'item': item})


# def aboutus(request, id):  # Modify the view function to accept the parameter
#     aboutus_item = get_object_or_404(AboutUs, id=id)  # Get the AboutUs object based on the ID
#     return render(request, "aboutus.html", {'aboutus_item': aboutus_item})  # Pass the AboutUs object to the template


  
def google_auth_view(request):
    return redirect("home")  

# from django.shortcuts import get_object_or_404, redirect
# from django.contrib.auth import get_user_model

# def get_menu_context(request, menu_item):
#     if not request.user.is_authenticated:
#         # Redirect to login page if not authenticated
#         return redirect('login')  # Replace 'login' with your login view name

#     redirect_url = menu_item.read_more_link
#     # ... other context data ...
#     context = {
#         'menu': menu_item,
#         'redirect_url': redirect_url,
#         # ... other context data ...
#     }
#     return context



# def story(request, name):
#         # print(name)
#         menu1=get_object_or_404(AboutUs,name=name)
#         return render(request, "story.html", {'menu1': menu1})


