from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from .models import Product


#register a user

class CreateUserForm(UserCreationForm):


    class Meta:
 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__()

        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["username"].widget.attrs['class'] = "input-class"
        self.fields["email"].widget.attrs['class'] = "input-class"
        self.fields["password1"].widget.attrs['class'] = "input-class"
        self.fields["password2"].widget.attrs['class'] = "input-class"

        self.fields['username'].widget.attrs['id'] = 'fName'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['username'].widget.attrs['name'] = 'firstName'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['id'] = 'fName'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['name'] = 'firstName'
        self.fields['email'].widget.attrs['placeholder'] = 'email'

        self.fields['password1'].widget.attrs['id'] = 'fName'
        self.fields['password1'].widget.attrs['type'] = 'password'
        self.fields['password1'].widget.attrs['name'] = 'firstName'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['id'] = 'fName'
        self.fields['password2'].widget.attrs['type'] = 'password'
        self.fields['password2'].widget.attrs['name'] = 'firstName'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

#login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'type' :'text', 'name ': 'firstName', 'id' : "fName", 'placeholder' : "Username", 'class' :"input-class"}))
    password = forms.CharField(widget=PasswordInput(attrs={'type' :'password', 'name ': 'firstName', 'id' : "fName", 'placeholder' : "Password", 'class' :"input-class"}))


#create a product

class addProduct(forms.ModelForm):

    class Meta:

        model = Product
        fields =  '__all__'  

