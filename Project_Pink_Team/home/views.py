#from django.contrib.auth.models import User 
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import TemplateView
from .models import User, Usuario , Materia_Actual, Historial_Materias, Escuela, Grupo, Periodo
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core import serializers
from .forms import Update_Calificacion, RegistroForm

from .forms import UpdateUserForm, CreateUserForm
from .forms import UpdateGrupoForm, CreateGrupoForm
from .forms import UpdateUsuarioForm, CreateUsuarioForm
from .forms import UpdateEscuelaForm, CreateEscuelaForm
from .forms import UpdateMateria_ActualForm, CreateMateria_ActualForm
from .forms import UpdatePeriodoForm, CreatePeriodoForm
from .forms import UpdateHistorial_MateriasForm, CreateHistorial_MateriasForm
#from django.shortcuts import get_object_or_404
#from django.conf import settings
# Create your views here.

# Vista inicial con login
class Index(generic.TemplateView):
    template_name = "home/index.html"
   # model = Usuario

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

#############         Vista Iniciar del docente
@permission_required('home.is_teacher')
def Home_Docente(request):
    status_list = Usuario.objects.all()
    status_filter = status_list.filter(user=request.user)
    return render(request, 'home/home_docente.html',{'filter': status_filter})

#Vista grupo del docente
@permission_required('home.is_teacher')
def Grupo_Docente(request):
    conectedu = Usuario.objects.all()
    filtercu = conectedu.filter(user = request.user)
    status_list = Usuario.objects.all().exclude(user=request.user)
    return render(request, 'home/grupo_docente.html',{'filter': status_list,'ufilter': filtercu})

class VistaDetalleAlumno(generic.DetailView):
    template_name = "home/detalle_alumno.html"
    model = Usuario

class VistaUpdateCalificacion(generic.UpdateView):
    template_name = "home/update_calificacion.html"
    model = Materia_Actual
    form_class = Update_Calificacion
    success_url = reverse_lazy("home:grupo_docente")




#Vista reporte del docente
@permission_required('home.is_teacher')
def Reporte_Docente(request):
    return render(request, 'home/reporte_docente.html')

#Vista historial del docente
@permission_required('home.is_teacher')
def Historial_Docente(request):
    return render(request, 'home/historial_docente.html')



################          Vista inicial de administrador     #############################
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
    

############################Vistas de la tabla User#########################################
class VistaTablaUser(generic.ListView):
    template_name = "home/tabla_user.html"
    model = User

class VistaDetalleUser(generic.DetailView):
    template_name = "home/detalle_user.html"
    model = User

class VistaUpdateUser(generic.UpdateView):
    template_name = "home/update_user.html"
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy("home:tabla_user")

class VistaDeleteUser(generic.DeleteView):
    template_name = "home/delete_user.html"
    model = User
    success_url = reverse_lazy("home:tabla_user")

class VistaCreateUser(generic.CreateView):
    template_name = "home/create_user.html"
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy("home:consulta_administrador")
###########################################################################################GrupoAdmin
class VistaTablaGrupo(generic.ListView):
    template_name = "home/tabla_grupo.html"
    model = Grupo

class VistaDetalleGrupo(generic.DetailView):
    template_name = "home/detalle_grupo.html"
    model = Grupo

class VistaUpdateGrupo(generic.UpdateView):
    template_name = "home/update_grupo.html"
    model = Grupo
    form_class = UpdateGrupoForm
    success_url = reverse_lazy("home:tabla_grupo")

class VistaDeleteGrupo(generic.DeleteView):
    template_name = "home/delete_grupo.html"
    model = Grupo
    success_url = reverse_lazy("home:tabla_grupo")

class VistaCreateGrupo(generic.CreateView):
    template_name = "home/create_grupo.html"
    model = Grupo
    form_class = CreateGrupoForm
    success_url = reverse_lazy("home:consulta_administrador")
###########################################################################################UsuarioAdmin
class VistaTablaUsuario(generic.ListView):
    template_name = "home/tabla_usuario.html"
    model = Usuario

class VistaDetalleUsuario(generic.DetailView):
    template_name = "home/detalle_usuario.html"
    model = Usuario

class VistaUpdateUsuario(generic.UpdateView):
    template_name = "home/update_usuario.html"
    model = Usuario
    form_class = UpdateUsuarioForm
    success_url = reverse_lazy("home:tabla_usuario")

class VistaDeleteUsuario(generic.DeleteView):
    template_name = "home/delete_usuario.html"
    model = Usuario
    success_url = reverse_lazy("home:tabla_usuario")

class VistaCreateUsuario(generic.CreateView):
    template_name = "home/create_usuario.html"
    model = Usuario
    form_class = CreateUsuarioForm
    success_url = reverse_lazy("home:consulta_administrador")

###########################################################################################EscuelaAdmin
class VistaTablaEscuela(generic.ListView):
    template_name = "home/tabla_escuela.html"
    model = Escuela

class VistaDetalleEscuela(generic.DetailView):
    template_name = "home/detalle_escuela.html"
    model = Escuela

class VistaUpdateEscuela(generic.UpdateView):
    template_name = "home/update_escuela.html"
    model = Escuela
    form_class = UpdateEscuelaForm
    success_url = reverse_lazy("home:tabla_escuela")

class VistaDeleteEscuela(generic.DeleteView):
    template_name = "home/delete_Escuela.html"
    model = Escuela
    success_url = reverse_lazy("home:tabla_escuela")

class VistaCreateEscuela(generic.CreateView):
    template_name = "home/create_escuela.html"
    model = Escuela
    form_class = CreateEscuelaForm
    success_url = reverse_lazy("home:consulta_administrador")

###########################################################################################Materia_ActualAdmin
class VistaTablaMateria_Actual(generic.ListView):
    template_name = "home/tabla_materia_Actual.html"
    model = Materia_Actual

class VistaDetalleMateria_Actual(generic.DetailView):
    template_name = "home/detalle_materia_Actual.html"
    model = Materia_Actual

class VistaUpdateMateria_Actual(generic.UpdateView):
    template_name = "home/update_materia_Actual.html"
    model = Materia_Actual
    form_class = UpdateMateria_ActualForm
    success_url = reverse_lazy("home:tabla_materia_Actual")

class VistaDeleteMateria_Actual(generic.DeleteView):
    template_name = "home/delete_materia_Actual.html"
    model = Materia_Actual
    success_url = reverse_lazy("home:tabla_materia_Actual")

class VistaCreateMateria_Actual(generic.CreateView):
    template_name = "home/create_materia_Actual.html"
    model = Materia_Actual
    form_class = CreateMateria_ActualForm
    success_url = reverse_lazy("home:consulta_administrador")



###########################################################################################PeriodoAdmin


class VistaTablaPeriodo(generic.ListView):
    template_name = "home/tabla_periodo.html"
    model = Periodo

class VistaDetallePeriodo(generic.DetailView):
    template_name = "home/detalle_periodo.html"
    model = Periodo

class VistaUpdatePeriodo(generic.UpdateView):
    template_name = "home/update_periodo.html"
    model = Periodo
    form_class = UpdatePeriodoForm
    success_url = reverse_lazy("home:tabla_periodo")

class VistaDeletePeriodo(generic.DeleteView):
    template_name = "home/delete_periodo.html"
    model = Periodo
    success_url = reverse_lazy("home:tabla_periodo")

class VistaCreatePeriodo(generic.CreateView):
    template_name = "home/create_periodo.html"
    model = Periodo
    form_class = CreatePeriodoForm
    success_url = reverse_lazy("home:consulta_administrador")

###########################################################################################historial_MateriasAdmin


class VistaTablaHistorial_Materias(generic.ListView):
    template_name = "home/tabla_historial_Materias.html"
    model = Historial_Materias

class VistaDetalleHistorial_Materias(generic.DetailView):
    template_name = "home/detalle_historial_Materias.html"
    model = Historial_Materias

class VistaUpdateHistorial_Materias(generic.UpdateView):
    template_name = "home/update_historial_Materias.html"
    model = Historial_Materias
    form_class = UpdateHistorial_MateriasForm
    success_url = reverse_lazy("home:tabla_historial_Materias")

class VistaDeleteHistorial_Materias(generic.DeleteView):
    template_name = "home/delete_historial_Materias.html"
    model = Historial_Materias
    success_url = reverse_lazy("home:tabla_historial_Materias")

class VistaCreateHistorial_Materias(generic.CreateView):
    template_name = "home/create_historial_Materias.html"
    model = Historial_Materias
    form_class = CreateHistorial_MateriasForm
    success_url = reverse_lazy("home:consulta_administrador")








#Funcion para crear nuevo usuario
class Signup(generic.CreateView):
    template_name = "home/signup.html"
    form_class = RegistroForm

    def get_success_url(self):
        return reverse('home:index')

#Funcion para Error 404 (Page not Found)
class Error404View(TemplateView):
    template_name = "base/base2.html"


#########################################################################     VISTAS DEL ALUMNOS     
@permission_required('home.is_student')
def Home_Alumno(request):
    queryset = Usuario.objects.all()
    status_filter = queryset.filter(user=request.user)
    query_filter = Escuela.objects.all()
    status_fil = query_filter.filter()
    return render(request, 'home/home_alumno.html', {'filter':status_filter,'filterU':status_fil})

############################################################################  VISTA DEL AVANCE
#######  VISTA DEL AVANCE DEL CICLO DEL ESTUDIANTES 
@permission_required('home.is_student')
def Avance_Alumno(request):
    status_list = Usuario.objects.all()
    status_fil = status_list.filter(user=request.user)
    query_filter = Materia_Actual.objects.all()
    status_filter = query_filter.filter()
    return render(request, 'home/avance_alumno.html',{'filter':status_filter, 'filterU':status_fil})  
   # , pk
   # user_pk= User.objects.get(pk=pk)
   #,context={'user':user_pk}
############################################################################   HISTORIAL ALUMNO 
#Vista historial del alumno Historial_Materias
@permission_required('home.is_student')
def Historial_Alumno(request):
    status_list = Usuario.objects.all()
    status_fil = status_list.filter(user=request.user)
    queryset= Historial_Materias.objects.all()
    status_filter = queryset.filter()
    return render(request,'home/historial_alumno.html', {'filter':status_filter, 'filterU':status_fil})

#############################################################   IMPRIME MANUAL DE IMPRIMIR BOLETA 
@permission_required('home.is_student')
def Imprimir_Alumno(request):
    queryset = Usuario.objects.all()
    status_filter = queryset.filter(user=request.user)
    return render(request, 'home/imprimir_alumno.html', {'filter':status_filter})

def wsBoleta(request):
    data = serializers.serialize("json",Historial_Materias.objects.all())
    return HttpResponse(data, content_type="application/json")

#####################################################################################
      
    