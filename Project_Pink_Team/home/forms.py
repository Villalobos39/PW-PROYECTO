from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

from .models import User

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
            model = User
            fields = ("username",)
            fields_classes = {"username": UsernameField}