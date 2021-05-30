from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User, Grupo, Usuario, Escuela, Materia_Actual, Periodo, Historial_Materias

#admin.site.register(ExtendedUser, UserAdmin)
admin.site.register(User)
admin.site.register(Grupo)
admin.site.register(Usuario)
admin.site.register(Escuela)
admin.site.register(Materia_Actual)
admin.site.register(Periodo)
admin.site.register(Historial_Materias)



