from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import *

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class createpostform(forms.ModelForm):
    class Meta:
        model=createpost
        fields=['catagory','title','body','author','images','type']
        widgets={
          
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a Title'}),
            'body':forms.Textarea(attrs={'class':'form-control','style':'resize:none','placeholder':'Your Quote'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            'type':forms.TextInput(attrs={'class':'form-control','placeholder':'Type   i.e... happy sad etc'}),
        }


class User_detailsform(forms.ModelForm):
    class Meta:
        model=User_details
        fields=['About','image']
        widgets={
          
            'About':forms.TextInput(attrs={'class':'form-control'}),
           
        }
