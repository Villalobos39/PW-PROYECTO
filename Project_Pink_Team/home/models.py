from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime    
#buscar como pasar multiples campos en def_str
#nos aseguramos que los nombres de usuario sea facil identificar que rol tienen
class User(AbstractUser):
    pass

class Grupo(models.Model):
    nombre_grupo=models.CharField(max_length=50)
    turno=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_grupo

class Usuario(models.Model):
    MS_CHOICES = (
        ("Alumno", "Alumno"),
        ("Docente","Docente"),
        ("Administrador","Administrador"),
        ("Pendiente","Pendiente"),
    )
    tipo_de_usuario = models.CharField(max_length=20, choices = MS_CHOICES, default="Pendiente")
    # is_docente = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    # is_alumno = models.BooleanField(default=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono_casa = models.CharField(max_length=32)
    telefono_cel = models.CharField(max_length=32, default="default")
    titulo_docente = models.CharField(max_length=50)
    grado_alumno = models.CharField(max_length=20)
    curp = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(default=datetime.now, blank=True)
    register_timestamp = models.DateTimeField(auto_now_add=True)
    register_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# class Docente(models.Model):
#     user_docente = models.OneToOneField(User, on_delete = models.CASCADE)
#     telefono = models.CharField(max_length=32)
#     titulo = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
#     register_timestamp = models.DateTimeField(auto_now_add=True)
#     regidter_update = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username

# class Alumno(models.Model):
#     MS_CHOICES = (
#         ("Matutino", "Matutino"),
#         ("Vespertino","Vespertino"),
#         ("Pendiente","Pendiente"),
#     )
#     user_alumno = models.OneToOneField(User, on_delete = models.CASCADE)
#     docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
#     grado = models.IntegerField()
#     telefono = models.CharField(max_length=32)
#     curp = models.CharField(max_length=32)
#     direccion = models.CharField(max_length=50)
#     turno = models.CharField(max_length=10, choices = MS_CHOICES)
#     register_timestamp = models.DateTimeField(auto_now_add=True)
#     regidter_update = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username

# class Administrador(models.Model):
#     user_admin = models.OneToOneField(User, on_delete = models.CASCADE)
#     telefono = models.CharField(max_length=32)
#     puesto = models.CharField(max_length=32)
#     titulo = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
#     register_timestamp = models.DateTimeField(auto_now_add=True)
#     regidter_update = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username

class Escuela(models.Model):
    nombre_institucion=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    nivel_educativo=models.CharField(max_length=20)
    control=models.CharField(max_length=30)
    turno=models.CharField(max_length=10)
    clave=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_institucion

class Materia_Actual(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_materia=models.CharField(max_length=30)
    horario=models.CharField(max_length=30)
    b1=models.FloatField(default=0.0)
    b2=models.FloatField(default=0.0)
    b3=models.FloatField(default=0.0)
    b4=models.FloatField(default=0.0)
    b5=models.FloatField(default=0.0)
    promedio=models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre_materia

class Periodo(models.Model):
    nombre_periodo=models.CharField(max_length=40)
    inicio_periodo=models.CharField(max_length=30)
    fin_periodo=models.CharField(max_length=30)
   
    def __str__(self):
        return self.nombre_periodo

class Historial_Materias(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombre_materia=models.CharField(max_length=30)
    horario=models.CharField(max_length=30)
    b1=models.FloatField(default=0.0)
    b2=models.FloatField(default=0.0)
    b3=models.FloatField(default=0.0)
    b4=models.FloatField(default=0.0)
    b5=models.FloatField(default=0.0)
    promedio=models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre_materia