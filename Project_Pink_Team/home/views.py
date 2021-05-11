from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

# Vista inicial con login
class Index(generic.TemplateView):
    template_name = "home/index.html"

# Vista inicial del alumno
class Home_Alumno(generic.TemplateView):
    template_name = "home/home_alumno.html"

# Vista avance del alumno
class Avance_Alumno(generic.TemplateView):
    template_name = "home/avance_alumno.html"

# Vista historial del alumno
class Historial_Alumno(generic.TemplateView):
    template_name = "home/historial_alumno.html"

# Vista imprimir del alumno
class Imprimir_Alumno(generic.TemplateView):
    template_name = "home/imprimir_alumno.html"

# Vista inicial del docente
class Home_Docente(generic.TemplateView):
    template_name = "home/home_docente.html"

# Vista grupo del docente
class Grupo_Docente(generic.TemplateView):
    template_name = "home/grupo_docente.html"

# Vista historial del docente
class Historial_Docente(generic.TemplateView):
    template_name = "home/historial_docente.html"

# Vista reporte del docente
class Reporte_Docente(generic.TemplateView):
    template_name = "home/reporte_docente.html"

# Vista inicial del administrador
class Home_Administrador(generic.TemplateView):
    template_name = "home/home_administrador.html"

# Vista consulta del administrador
class Consulta_Administrador(generic.TemplateView):
    template_name = "home/consulta_administrador.html"

# Vista historial del administrador
class Historial_Administrador(generic.TemplateView):
    template_name = "home/historial_administrador.html"
