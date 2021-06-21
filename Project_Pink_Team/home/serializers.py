from rest_framework import serializers
from .models import Materia_Actual

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia_Actual
        fields = "__all__"