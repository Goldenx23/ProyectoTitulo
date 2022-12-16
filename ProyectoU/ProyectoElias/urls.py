"""ProyectoElias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Alumnado.views import index, inicio, AlumnosTodos, eliminar, agregar, editar, editarAlumno, usuariosTodos, eliminarUsuario, agregarUsuario, editarUsuario, editarEncargado
from Alumnado.views import indexForm, alumnosVista, AlumnoListado, aceptarSolicitud, rechazarSolicitud, alumno_detalle, usuarioVista, listarAlumno, listarUsuario, solicitudAlumno, estadoSolicitud, horarioDae, paginaLogin, paginaLoginDae, agregarSolicitud, LoginAlumnoMantenedor, LoginUsuarioMantenedor
from Alumnado.views import AlumnoListado, alumno_detalle
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('login/', paginaLogin, name = 'login'),
    path('loginDae/', paginaLoginDae, name="loginDae"),
    path('indexForm/', indexForm),
    path('solicitudAlumno/', solicitudAlumno),
    path('agregarSolicitud/',agregarSolicitud),
    path('estadoSolicitud/', estadoSolicitud),
    path('horarioDae/',horarioDae),
    path('index/',index),
    path('index/loginAlumnos/', LoginAlumnoMantenedor),
    path('index/loginUsuario/', LoginUsuarioMantenedor),
    path('loginAlumnos/Alumnos/', AlumnosTodos),
    path('loginAlumnos/eliminar/<int:id>', eliminar),
    path('addAlumno/', agregar),
    path('loginAlumnos/modificar/<int:id>',editar),
    path('editarAlumno/',editarAlumno),
    path('alumno/', alumnosVista),
    path('alumnosL/', AlumnoListado.as_view()),
    path('alumnosL/<int:pk>', alumno_detalle.as_view()),
    path('usuario/', usuarioVista),
    path('loginUsuario/usuarios/',usuariosTodos),
    path('loginUsuario/eliminarUsuario/<int:id>',eliminarUsuario),
    path('addUsuario/',agregarUsuario),
    path('loginUsuario/modificarEncargado/<int:id>',editarEncargado),
    path('editarUsuario/',editarUsuario),
    path('buscarAlumno/', listarAlumno),
    path('buscarUsuario/', listarUsuario),
    path('aceptarSolicitud/<int:id>', aceptarSolicitud),
    path('rechazarSolicitud/<int:id>', rechazarSolicitud)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)