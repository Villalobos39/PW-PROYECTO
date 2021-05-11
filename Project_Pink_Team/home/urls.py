from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('index/', views.Index.as_view(), name="index"),
    path('home_alumno/', views.Home_Alumno.as_view(), name="home_alumno"),
    path('avance_alumno/', views.Avance_Alumno.as_view(), name="avance_alumno"),
    path('historial_alumno/', views.Historial_Alumno.as_view(), name="historial_alumno"),
    path('imprimir_alumno/', views.Imprimir_Alumno.as_view(), name="imprimir_alumno"),
    path('home_docente/', views.Home_Docente.as_view(), name="home_docente"),
    path('grupo_docente/', views.Grupo_Docente.as_view(), name="grupo_docente"),
    path('historial_docente/', views.Historial_Docente.as_view(), name="historial_docente"),
    path('reporte_docente/', views.Reporte_Docente.as_view(), name="reporte_docente"),
    path('home_administrador/', views.Home_Administrador.as_view(), name="home_administrador"),
    path('historial_administrador/', views.Historial_Administrador.as_view(), name="historial_administrador"),
    path('consulta_administrador/', views.Consulta_Administrador.as_view(), name="consulta_administrador"),
]