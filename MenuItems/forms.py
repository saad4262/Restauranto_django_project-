from django import forms
from .models import dineIn

class DineInForm(forms.ModelForm):
    class Meta:
        model = dineIn
        fields = ['name', 'email', 'number', 'table_no', 'people', 'requests']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-white rounded-md border-gray-300 text-black px-2 py-1', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-white rounded-md border-gray-300 text-black px-2 py-1', 'placeholder': 'Enter email'}),
            'number': forms.TextInput(attrs={'class': 'w-full bg-white rounded-md border-gray-300 text-black px-2 py-1', 'placeholder': 'Enter number'}),
            'table_no': forms.Select(choices=[(1, '1 Person'), (2, '2 People'), (3, '3 People'), (4, '4 People'), (5, '5 People'), (6, '6 People'), (7, '7 People'), (8, '8 People'), (9, '9 People')],attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}),
            'people': forms.TextInput(attrs={'class': 'w-full bg-white rounded-md border-gray-300 text-black px-2 py-1', 'placeholder': 'Enter number of People'}),
            'requests': forms.TextInput(attrs={'class': 'w-full bg-white rounded-md border-gray-300 text-black px-2 py-1', 'placeholder': 'Any requests'}),
        }
