from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [ 'image','name', 'email', 'phone', 'gender', 'job_type', 'resume']
        # widgets = {
        #     'image': forms.ClearableFileInput(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'name': forms.TextInput(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'email': forms.EmailInput(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'phone': forms.TextInput(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'gender': forms.Select(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'job_type': forms.Select(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        #     'resume': forms.FileInput(attrs={'class': 'pl-2 w-full outline-none border-none mb-8 py-2 px-3 rounded-2xl'}),
        # }
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'hidden pl-2 w-full outline-none border-none mb-2 py-2 px-3 rounded-lg'
            }),
            'name': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'Enter your email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'Enter your phone number'
            }),
            'gender': forms.Select(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'Select your gender'
            }),
            'job_type': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'job type'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded-xl py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
                'placeholder': 'Upload your resume'
            }),
        }
