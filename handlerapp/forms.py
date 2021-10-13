from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class signupform(forms.Form):
    Name=forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"})
    )
    Firstname = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name"})
    )
    lastname = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name"})
    )
    Email=forms.CharField(
        label="Email",
        max_length=100,
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"})
    )
    Password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"})
    )
    def clean_Name(self):
        username = self.cleaned_data.get('Name')
        print(username)
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('User is already exists')
        return username

    def clean_Password(self):
        data=self.cleaned_data.get('Password')
        print(data)
        if len(data)<8:
            raise forms.ValidationError("password length must be 8")
        return data

    def clean_Email(self):
    # Check that email is not duplicate
        username = self.cleaned_data.get('Name')
        email = self.cleaned_data.get('Email')
        print("y1",email,username)
        users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
        if users:
            print("y2")
            raise forms.ValidationError("A user with that email already exists.")
        return email.lower()




class loginform(forms.Form):
    Username=forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"})
    )
    Password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"})
    )
    def clean_Password(self):
        username = self.cleaned_data.get('Username')
        password=self.cleaned_data.get('Password')
        user = authenticate(username=username, password=password)
        print(user)
        if user==None:
            raise forms.ValidationError("Username and Password did not match")
        return username,password


