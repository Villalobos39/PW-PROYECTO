import django_filters
from .models import Usuario

class BoletaAlumno(django_filters.FilterSet):
    
    class Meta:
        model = Usuario
        fields = {
            'curp':['icontains'],
        }