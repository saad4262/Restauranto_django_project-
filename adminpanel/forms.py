# forms.py
from django import forms
from .models import ChefModels

class ChefForm(forms.ModelForm):
    class Meta:
        model = ChefModels
        fields = ['name', 'title', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4', 'placeholder': 'Enter Name'}),
            'title': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4', 'placeholder': 'Enter Title'}),
            'image': forms.FileInput(attrs={'id': 'id_image', 'accept': 'image/*', 'class': 'hidden', 'onchange': 'loadFile(event)'}),
           }