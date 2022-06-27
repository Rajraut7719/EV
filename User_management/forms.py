from dataclasses import field
from email.policy import default
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm
# Registration Form
class RegisterForm(UserCreationForm):
    username=forms.CharField(help_text='Enter full name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}))
    # check=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model=User
        fields=['username','mobile','email']

# Login Form
class Login_Form(AuthenticationForm):
    username=forms.CharField(error_messages={'required':'Enter Username'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(error_messages={'required':'Enter Password'},widget=forms.PasswordInput(attrs={'class':'form-control ','placeholder':'Password'}))


# Change Password
class Password_change_Form(PasswordChangeForm):
    old_password=forms.CharField(error_messages={'required':'Enter old Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(error_messages={'required':'Enter password'},label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(error_messages={'required':'Enter Conform password'},label='Conform Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))



