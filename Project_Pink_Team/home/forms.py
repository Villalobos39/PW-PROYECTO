from django import forms
<<<<<<< Updated upstream
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

=======
from django.contrib.auth.forms import UserCreationForm, UsernameField  
from django.contrib.auth import get_user_model


>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======



##grupo

class UpdateGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        exclude = 'id',

class CreateGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        exclude = 'id',

##Usuario

class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = 'id',

class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = 'id',


##Escuela

class UpdateEscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = "__all__"
        exclude = 'id',

class CreateEscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = "__all__"
        exclude = 'id',

##MateriaActual

class UpdateMateria_ActualForm(forms.ModelForm):
    class Meta:
        model = Materia_Actual
        fields = "__all__"
        exclude = 'id',

class CreateMateria_ActualForm(forms.ModelForm):
    class Meta:
        model = Materia_Actual
        fields = "__all__"
        exclude = 'id',


##Periodo

class UpdatePeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = "__all__"
        exclude = 'id',

class CreatePeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = "__all__"
        exclude = 'id',


##Historial_Materias

class UpdateHistorial_MateriasForm(forms.ModelForm):
    class Meta:
        model = Historial_Materias
        fields = "__all__"
        exclude = 'id',

class CreateHistorial_MateriasForm(forms.ModelForm):
    class Meta:
        model = Historial_Materias
        fields = "__all__"
        exclude = 'id',
>>>>>>> Stashed changes
