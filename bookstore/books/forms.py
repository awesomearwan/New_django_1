from django import forms
from .models import Contact, profile    



class AddProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name', 'email', 'address', 'about']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about yourself'}),
        }
        