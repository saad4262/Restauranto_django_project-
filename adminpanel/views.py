from django.shortcuts import render,redirect, redirect, get_object_or_404
from chefs.models import ChefsModel
from django.views.decorators.http import require_POST

# Create your views here.
from django.contrib.auth import authenticate, login, logout 
from help.models import Help
from help.forms import HelpForm
from chefs.models import ChefsModel
from career.models import Applicant
from django.http import JsonResponse
from home.models import Reservation
from django.shortcuts import render, redirect
from .forms import ChefForm
from .models import ChefModels
from contact.models import Contact
from .models import AdminProfile
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from MenuItems.models import Product
from MenuItems.models import Customer, Order, OrderItem, shipping_address
# from MenuItems.views import *





def index(request):
    return render(request, 'home.html')

# @login_required
def adminpanel(request):
        if request.method == 'POST':
          form = ChefForm(request.POST, request.FILES)
          if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to success URL
        else:
            form = ChefForm()
        # return render(request, 'your_template.html', {})
        product_messages = Product.objects.all()
        category = request.GET.get('category')
        search_query = request.GET.get('search')  # New: Get the search query from the request

        if category:
          product_messages = product_messages.filter(category=category)

        if search_query:  # New: Filter products by name if search query exists
             product_messages = product_messages.filter(product_name__icontains=search_query)
        context = {
            'help' : Help.objects.all(),
            # 'chefsData' : ChefsModel.objects.all(),
              'emp' : ChefModels.objects.all(),
            'applicants' : Applicant.objects.all(),
            'reservation' : Reservation.objects.all(),
            'contacts': Contact.objects.all(),
            'form': form,
            'admindata': AdminProfile.objects.all(),
              'products': Product.objects.all(),
              'product_messages': product_messages,
              'category': category,
            #   'shipping_address': shipping_address.objects.all(),
              
            #   'Order': Order.objects.all(),
              
            #   'OrderItem': OrderItem.objects.all()
              
              
              
              

            
                }
        return render(request, "adminpanel.html",context)
        # if request.method == "POST" and request.is_ajax():
        #     applicant_id = request.POST.get("applicant_id")
        #     try:
        #       applicant = Applicant.objects.get(pk=applicant_id)
        #       applicant.selected = True
        #       applicant.save()
        #       return JsonResponse({"success": True})
        #     except Applicant.DoesNotExist:
        #       return JsonResponse({"success": False, "error": "Applicant does not exist"})
        # return JsonResponse({"success": False, "error": "Invalid request"})
         
  
def google_auth_view(request):
    return redirect("home")  


def user_logout(request):
    logout(request)
    return redirect('home')





def Admin_Login(request):
     if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')

        # Set your predefined admin username and password
        admin_username = 'admin'
        admin_password = 'password123'

        if username == admin_username and password == admin_password:
            # Successful login
            return redirect('adminpanel')  # Redirect to a dashboard or another page
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password')

   
     return render(request, 'adminLogin.html')



# def delete_profile(request, profile_id):
#     profile = get_object_or_404(ChefModels, id=profile_id)
#     profile.delete()
#     return redirect('login')
 

# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import ChefModels

# def edit_chef(request, pk):
#     chef = get_object_or_404(ChefModels, pk=pk)
    
#     if request.method == 'POST':
#         chef.name = request.POST.get('name')
#         chef.title = request.POST.get('title')
#         image = request.FILES.get('image')
#         if image:
#             chef.image = image
#         chef.save()
#         return JsonResponse({'message': 'Chef details updated successfully'})
    
#     return render(request, 'adminpanel.html', {'chef': chef})



# def edit(request):
#     emp = ChefModels.objects.all()
#     context = {
#         'emp': emp
#     }
#     return render(request, 'edit.html', context)

# def update(request, id):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')

#         emp = ChefModels(
#         id = id,
#         name = name,
#         email = email,
#         address = address,
#         phone = phone

#         )
#         emp.save()
#         return redirect('home')
    
#     return redirect(request, 'index.html')


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        image = request.FILES.get('image')  # Corrected here

        emp = ChefModels(
            image=image,
            name=name,
            title=title,
        )
        emp.save()
        return redirect('home')

    return render(request, 'add.html')

def edit(request):
    emp = ChefModels.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'edit.html', context)

def update(request, id):
    emp = get_object_or_404(ChefModels, id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        image = request.FILES.get('image')  # Corrected here

        # Update fields only if they are provided in the request
        if image:
            emp.image = image
        emp.name = name
        emp.title = title
        
        emp.save()
        return redirect('home')
    
    return redirect('home')


def delete_employee(request, id):
    employee = get_object_or_404(ChefModels, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('login')
    return render(request, 'delete_employee.html', {'employee': employee})




class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Check if the user is authenticated
        if not request.user.is_authenticated and not request.path.startswith(reverse('adminLogin')):
            # Redirect to the login page if the user is not authenticated
            return redirect('adminLogin')
        return response
