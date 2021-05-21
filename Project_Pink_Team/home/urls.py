from django.urls import path
from django.contrib.auth import views as auth_views

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('home_alumno/', views.Home_Alumno, name='home_alumno'),
    path('avance_alumno/', views.Avance_Alumno, name="avance_alumno"),
    path('historial_alumno/', views.Historial_Alumno, name="historial_alumno"),
    path('imprimir_alumno/', views.Imprimir_Alumno, name="imprimir_alumno"),
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
    path('casa/', views.Casa, name='casa')
]