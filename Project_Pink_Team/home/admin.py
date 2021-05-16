from django.contrib import admin

# Register your models here.
from .models import User
from .models import Grupo
from .models import Usuario
from .models import Escuela
from .models import Materia_Actual
from .models import Periodo
from .models import Historial_Materias

admin.site.register(User)
admin.site.register(Grupo)
admin.site.register(Usuario)
admin.site.register(Escuela)
admin.site.register(Materia_Actual)
admin.site.register(Periodo)
admin.site.register(Historial_Materias)
