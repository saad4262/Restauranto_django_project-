from django.shortcuts import render,redirect
from chefs.models import ChefsModel
# Create your views here.
from .forms import ApplicantForm  # Import your form class
from .models import Applicant 

def index(request):
    return render(request, 'home.html')

def career(request):
        
        # chefsData=ChefsModel.objects.all()
        if request.method == 'POST':
          form = ApplicantForm(request.POST, request.FILES)  # Pass both POST data and FILES (for file uploads) to the form
          if form.is_valid():
            # Process the form data
            form.save()  # Save the form data to the database or perform any other necessary actions
            return redirect('signup')  # Redirect to a success page after form submission
        else:
          form = ApplicantForm()  # 
        return render(request, "career.html", {'form': form})
  
def google_auth_view(request):
    return redirect("home")  

