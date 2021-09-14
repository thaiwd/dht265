from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","captcha")
        field_classes = {'username': UsernameField}

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ('full_name',"address", "year_birth", 'about')