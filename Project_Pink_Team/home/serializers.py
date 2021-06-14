from rest_framework import serializers

from .models import User, Usuario , Materia_Actual, Historial_Materias, Escuela, Grupo, Periodo

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = "__all__"