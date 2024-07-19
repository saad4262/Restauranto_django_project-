
from django import forms
from home.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name','phone_number', 'email', 'num_people', 'date', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Render the date field as a date input
            'phone_number': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'id': 'grid-phone-number', 'placeholder': 'Phone Number'}),
            'name': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'id': 'grid-first-name', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'id': 'grid-email', 'placeholder': 'Email'}),
            'num_people': forms.Select(choices=[(1, '1 Person'), (2, '2 People'), (3, '3 People'), (4, '4 People'), (5, '5 People'), (6, '6 People'), (7, '7 People'), (8, '8 People'), (9, '9 People')], attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'id': 'grid-state'}),
            'date': forms.DateInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'id': 'grid-date', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'message': forms.Textarea(attrs={'class': 'w-full h-32 p-2 border border-gray-300 rounded-md text-base focus:outline-none focus:border-blue-500', 'id': 'myTextarea', 'placeholder': 'Special Request', 'rows': '4'}),

        }



from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipient']
        widgets = {
            'recipient': forms.EmailInput(attrs={'class': 'subscribe-input', 'placeholder': 'Your e-mail'}),
        }
