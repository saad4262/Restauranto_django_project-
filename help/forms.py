from django import forms
from .models import Help

class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
                'placeholder': 'Enter your name',
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
                'placeholder': 'Enter your email',
                'id': 'email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out',
                'placeholder': 'Enter your message',
                'id': 'message'
            }),
        }
