from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy

<<<<<<< Updated upstream
=======
from .forms import UpdateUserForm, CreateUserForm
from .forms import UpdateGrupoForm, CreateGrupoForm
from .forms import UpdateUsuarioForm, CreateUsuarioForm
from .forms import UpdateEscuelaForm, CreateEscuelaForm
from .forms import UpdateMateria_ActualForm, CreateMateria_ActualForm
from .forms import UpdatePeriodoForm, CreatePeriodoForm
from .forms import UpdateHistorial_MateriasForm, CreateHistorial_MateriasForm



#Cosas del API
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from home.serializers import UserSerializer, UsuarioSerializer, Materia_ActualSerializer, EscuelaSerializer, GrupoSerializer,PeriodoSerializer


#from django.shortcuts import get_object_or_404
#from django.conf import settings
>>>>>>> Stashed changes
# Create your views here.

# Vista inicial con login
class Index(generic.TemplateView):
    template_name = "home/index.html"
<<<<<<< Updated upstream
=======
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





>>>>>>> Stashed changes

# Vista inicial del alumno
class Home_Alumno(generic.TemplateView):
    template_name = "home/home_alumno.html"

<<<<<<< Updated upstream
# Vista avance del alumno
class Avance_Alumno(generic.TemplateView):
    template_name = "home/avance_alumno.html"
=======
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
# Vista historial del administrador
class Historial_Administrador(generic.TemplateView):
    template_name = "home/historial_administrador.html"
=======
#####################################################################################
#Endpoints....
@api_view(["GET", "POST"])
def List_User(request):
    #list
    if request.method == "GET":
        queryset = User.objects.all()
        data = UserSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = UserSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def List_Usuario(request):
    #list
    if request.method == "GET":
        queryset = Usuario.objects.all()
        data = UsuarioSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = UsuarioSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def List_Materia_Actual(request):
    #list
    if request.method == "GET":
        queryset = Materia_Actual.objects.all()
        data = Materia_ActualSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = Materia_ActualSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def List_Escuela(request):
    #list
    if request.method == "GET":
        queryset = Escuela.objects.all()
        data = EscuelaSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = EscuelaSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def List_Grupo(request):
    #list
    if request.method == "GET":
        queryset = Grupo.objects.all()
        data = GrupoSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = GrupoSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def List_Periodo(request):
    #list
    if request.method == "GET":
        queryset =Periodo.objects.all()
        data = PeriodoSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = PeriodoSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


      
    
>>>>>>> Stashed changes
