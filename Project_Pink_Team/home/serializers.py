from rest_framework import serializers

from .models import User, Usuario , Materia_Actual, Historial_Materias, Escuela, Grupo, Periodo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =  "__all__"

class Materia_ActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia_Actual
        fields =  "__all__"

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields =  "__all__"

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = "__all__"

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = "__all__"
