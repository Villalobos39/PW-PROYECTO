from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import User
from datetime import datetime    
from django.utils.translation import ugettext as _
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

    MS_GRADOS = (
        ("Primer grado", "Primer grado"),
        ("Segundo grado","Segundo grado"),
        ("Tercer grado","Tercer grado"),
        ("Cuarto grado","Cuarto grado"),
        ("Quinto grado","Quinto grado"),
        ("Sexto grado","Sexto grado"),
        ("Pendiente","Pendiente"),
    )
    
    tipo_de_usuario = models.CharField(max_length=20, choices = MS_CHOICES, default="Pendiente")
    is_docente = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_alumno = models.BooleanField(default=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono_casa = models.CharField(max_length=32, default="pendiente")
    telefono_cel = models.CharField(max_length=32, default="pendiente")
    titulo_docente = models.CharField(max_length=50, default="pendiente")
    grado_alumno = models.CharField(max_length=20, choices = MS_GRADOS, default="Pendiente")
    curp = models.CharField(max_length=20, default="pendiente")
    direccion = models.CharField(max_length=50, default="pendiente")
    fecha_nacimiento = models.DateTimeField(default=datetime.now, blank=True)
    register_timestamp = models.DateTimeField(auto_now_add=True)
    register_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# Se agregan permisos a la clase Usuario
    class Meta:
        permissions = (
            ('is_teacher', _('Is Teacher')),
            ('is_student', _('Is Student')),
            ('is_admin', _('Is Admin')),
        )

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
    MS_MATERIAS = (
        #grado 1
        ("Español 1", "Español 1"),
        ("Matemáticas 1","Matemáticas 1"),
        ("Exploración de la Naturaleza y la Sociedad 1","Exploración de la Naturaleza y la Sociedad 1"),
        ("Formación Cívica y Ética 1","Formación Cívica y Ética 1"),
        #grado 2
        ("Español 2", "Español 2"),
        ("Matemáticas 2","Matemáticas 2"),
        ("Exploración de la Naturaleza y la Sociedad 2","Exploración de la Naturaleza y la Sociedad 2"),
        ("Formación Cívica y Ética 2","Formación Cívica y Ética 2"),
        #grado 3
        ("Español 3", "Español 3"),
        ("Matemáticas 3","Matemáticas 3"),
        ("Ciencias Naturales 1","Ciencias Naturales 1"),
        ("La Entidad donde vivo","La Entidad donde vivo"),
        ("Formación Cívica y Ética 3","Formación Cívica y Ética 3"),
        #grado 4
        ("Español 4", "Español 4"),
        ("Matemáticas 4","Matemáticas 4"),
        ("Ciencias Naturales 2","Ciencias Naturales 2"),
        ("Geografía 1","Geografía 1"),
        ("Historia 1","Historia 1"),
        ("Formación Cívica y Ética 4","Formación Cívica y Ética 4"),
        #grado 5
        ("Español 5", "Español 5"),
        ("Matemáticas 5","Matemáticas 5"),
        ("Ciencias Naturales 3","Ciencias Naturales 3"),
        ("Geografía 2","Geografía 2"),
        ("Historia 2","Historia 2"),
        ("Formación Cívica y Ética 5","Formación Cívica y Ética 5"),
        #grado 6
        ("Español 6", "Español 6"),
        ("Matemáticas 6","Matemáticas 6"),
        ("Ciencias Naturales 4","Ciencias Naturales 4"),
        ("Geografía 3","Geografía 3"),
        ("Historia 3","Historia 3"),
        ("Formación Cívica y Ética 6","Formación Cívica y Ética 6"),
        ("Pendiente","Pendiente"),
    )
    MS_HORARIOS = (
        #matutinos
        ("8:00-9:00", "8:00-9:00"),
        ("9:00-10:00", "9:00-10:00"),
        ("10:00-11:00", "10:00-11:00"),
        ("11:30-12:30", "11:30-12:30"),
        ("12:30-13:30", "12:30-13:30"),
        ("13:30-14:30", "13:30-14:30"),
        #vespertinos
        ("13:30-14:00", "13:30-14:00"),
        ("14:00-15:00", "14:00-15:00"),
        ("15:00-16:00", "15:00-16:00"),
        ("16:30-17:00", "16:00-17:00"),
        ("17:00-18:30", "17:30-18:30"),
        ("18:30-19:30", "17:30-18:30"),
        ("Pendiente","Pendiente"),
    )
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_materia=models.CharField(max_length=50, choices = MS_MATERIAS, default="Pendiente")
    horario=models.CharField(max_length=50, choices = MS_HORARIOS, default="Pendiente")
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
    nombre_materia=models.CharField(max_length=50)
    horario=models.CharField(max_length=50)
    b1=models.FloatField(default=0.0)
    b2=models.FloatField(default=0.0)
    b3=models.FloatField(default=0.0)
    b4=models.FloatField(default=0.0)
    b5=models.FloatField(default=0.0)
    promedio=models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre_materia