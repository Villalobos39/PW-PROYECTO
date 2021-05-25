from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('avance_alumno/', views.Avance_Alumno, name="avance_alumno"),
    path('home_docente/', views.Home_Docente, name='home_docente'),
    path('grupo_docente/', views.Grupo_Docente, name="grupo_docente"),
    path('historial_docente/', views.Historial_Docente, name="historial_docente"),
    path('reporte_docente/', views.Reporte_Docente, name="reporte_docente"),
    path('home_administrador/', views.Home_Administrador, name="home_administrador"),
    path('historial_administrador/', views.Historial_Administrador, name="historial_administrador"),
    path('consulta_administrador/', views.Consulta_Administrador, name="consulta_administrador"),

    # Url para inicio y creacion de sesion
    path('login/', auth_views.LoginView.as_view(), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('signup/', views.Signup.as_view(), name = "signup"),
    
    #Esta vista nos va a redirigir a otra segun el tipo de usuario
    path('casa/', views.Casa, name='casa'),

    #ALUMNOS URLS MODIFICADOS 
    path('home_alumno/', views.Home_Alumno, name='home_alumno'),
    # AVANCE URL DE LOS ALUMNOS 
    path('avance_alumno/',views.Avance_Alumno, name="avance_alumno"),
    # HISTORIAL DESPLEJA UN KARDEX GENERAL  
    path('historial_alumno/', views.Historial_Alumno, name="historial_alumno"),
    # ES UN  MANUEAL DE COMO IMPRIMIR LA PANTALLA 
     path('imprimir_alumno/', views.Imprimir_Alumno, name="imprimir_alumno"), 
    # Boleta_AlumnoView json 
    path('ws/vl/boleta', views.wsBoleta , name ="wsvlboleta"),

    # path('avance_alumno/',permission_required('home.is_student')(views.Avance_AlumnoView.as_view()), name="avance_alumno"),
    
]