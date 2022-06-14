from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import Profile
from app.models import Review



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields=['username','email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    profileImage = forms.ImageField(required=True)
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}), required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    country = forms.CharField(max_length=50)


    class Meta:
        model = Profile
        fields=['profileImage', 'firstName', 'lastName','bio','country']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = User
        fields=['username', 'username']

class ReviewForm(forms.ModelForm):
     class Meta:
        model = Review
        exclude = ['project', 'user']