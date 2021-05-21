from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import TemplateView

from .forms import CustomUserCreationForm
# Create your views here.

# Vista inicial con login
class Index(generic.TemplateView):
    template_name = "home/index.html"

#Funcion para redireccionar segun el tipo de usuario
@login_required
def Casa(request):
    user = request.user
    if user.has_perm('home.is_teacher'):
        return redirect(reverse('home:home_docente'))
    elif user.has_perm('home.is_student'):
        return redirect(reverse('home:home_alumno'))
    elif user.has_perm('home.is_admin'):
        return redirect(reverse('home:home_administrador'))
    else:
        return render(request, template_name='home/home_pendiente.html')

#Vista Iniciar del docente
@permission_required('home.is_teacher')
def Home_Docente(request):
    return render(request, 'home/home_docente.html')

#Vista grupo del docente
@permission_required('home.is_teacher')
def Grupo_Docente(request):
    return render(request, 'home/grupo_docente.html')

#Vista reporte del docente
@permission_required('home.is_teacher')
def Reporte_Docente(request):
    return render(request, 'home/reporte_docente.html')

#Vista historial del docente
@permission_required('home.is_teacher')
def Historial_Docente(request):
    return render(request, 'home/historial_docente.html')


#Vista inicial del alumno
@permission_required('home.is_student')
def Home_Alumno(request):
    return render(request, 'home/home_alumno.html')

#Vista avance del alumno
@permission_required('home.is_student')
def Avance_Alumno(request):
    return render(request, 'home/avance_alumno.html')

#Vista imprimir del alumno
@permission_required('home.is_student')
def Imprimir_Alumno(request):
    return render(request, 'home/imprimir_alumno.html')

#Vista historial del alumno
@permission_required('home.is_student')
def Historial_Alumno(request):
    return render(request, 'home/historial_alumno.html')


#Vista inicial de administrador
@permission_required('home.is_admin')
def Home_Administrador(request):
    return render(request, 'home/home_administrador.html')

#Vista consulta del administrador
@permission_required('home.is_admin')
def Consulta_Administrador(request):
    return render(request, 'home/consulta_administrador.html')

#Vista historial del administrador
@permission_required('home.is_admin')
def Historial_Administrador(request):
    return render(request, 'home/historial_administrador.html')


#Funcion para crear nuevo usuario
class Signup(generic.CreateView):
    template_name = "home/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('home:index')

#Funcion para Error 404 (Page not Found)
class Error404View(TemplateView):
    template_name = "home/404.html"
