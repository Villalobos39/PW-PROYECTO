from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

from .models import User, Usuario , Materia_Actual, Historial_Materias, Escuela, Grupo, Periodo

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
            model = User
            fields = ("username",)
            fields_classes = {"username": UsernameField}

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = 'id',

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = 'id',
