from django.shortcuts import render, redirect
from .serializers import AlumnoSerializar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Alumno, Carrera, Encargado, Usuario, Solicitud
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
# Create your views here.
alumnoid = {
    "id":0
}

def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def indexForm(request):
    return render(request, 'indexForm.html')

def estadoSolicitud(request):
    solicitudes = Solicitud.objects.filter(alumno_id=alumnoid['id'])
    data = {
        'solicitudes': solicitudes
    }
    return render(request, 'estadoSolicitud.html',data)

def solicitudAlumno(request):
    return render(request, 'solicitudAlumno.html')



def paginaLogin(request):
    if request.method == 'POST':
        try:
            detalleAlumno = Alumno.objects.get(correo=request.POST['correo'], contraseña=request.POST['contraseña'])
            print("Usuario=", detalleAlumno)
            alumnoid['id'] = detalleAlumno.id
            request.session['correo']=detalleAlumno.correo
            return redirect('/indexForm/')
        except Alumno.DoesNotExist as e:
            messages.add_message(request, messages.INFO, 'Correo o contraseña erronea.')
    return render(request,'login.html')

def paginaLoginDae(request):
    if request.method == 'POST':
        try:
            detalleDae = Usuario.objects.get(nombre_usuario=request.POST['nombre_usuario'], contraseña=request.POST['contraseña'])
            print("Usuario=", detalleDae)
            request.session['correo']=detalleDae.correo
            return redirect('/horarioDae/')
        except Usuario.DoesNotExist as e:
            messages.add_message(request, messages.INFO, 'Correo o contraseña erronea.')
            
    return render(request,'loginDae.html')

def aceptarSolicitud(request,id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.estado = "aceptado"
    solicitud.save()
    return redirect('/horarioDae/')

def rechazarSolicitud(request,id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.estado = "rechazado"
    solicitud.save()
    return redirect('/horarioDae/')

def LoginAlumnoMantenedor(request):
    if request.method == 'POST':
        try:
            detalleAlumno = Alumno.objects.get(correo=request.POST['correo'], contraseña=request.POST['contraseña'])
            print("Usuario=", detalleAlumno)
            alumnoid['id'] = detalleAlumno.id
            request.session['correo']=detalleAlumno.correo
            return redirect('/loginAlumnos/Alumnos/')
        except Alumno.DoesNotExist as e:
            messages.add_message(request, messages.INFO, 'Correo o contraseña erronea.')
    return render(request,'loginMantenedorAlum.html')

def LoginUsuarioMantenedor(request):
    if request.method == 'POST':
        try:
            detalleDae = Usuario.objects.get(nombre_usuario=request.POST['nombre_usuario'], contraseña=request.POST['contraseña'])
            print("Usuario=", detalleDae)
            request.session['nombre_usuario']=detalleDae.nombre_usuario
            return redirect('/loginUsuario/usuarios/')
        except Usuario.DoesNotExist as e:
            messages.add_message(request, messages.INFO, 'Correo o contraseña erronea.')
    return render(request,'loginMantenedorUser.html')


def horarioDae(request):
    solicitudes = Solicitud.objects.all()
    data = {
        'solicitudes': solicitudes
    }
    return render(request,'HorarioDae.html',data)

def listarAlumno(request):
    busqueda = request.POST['buscar']

    alumno = Alumno.objects.filter(
        Q(rut__contains = busqueda) |
        Q(nombre__contains = busqueda) |
        Q(apellidos__contains = busqueda) |
        Q(correo__contains = busqueda) |
        Q(contraseña__contains = busqueda) 
        )
    data = {'alumnos':alumno}

    return render(request, 'alumnos.html',data)

def listarUsuario(request):
    busqueda = request.POST['buscar']

    usuarios = Usuario.objects.filter(
        Q(nombre_usuario__contains = busqueda) |
        Q(contraseña__contains = busqueda) |
        Q(correo__contains = busqueda)
        )
    data = {'usuarios':usuarios}

    return render(request, 'usuarios.html',data)

def AlumnosTodos(request):
    alumnos = Alumno.objects.all()
    carreras = Carrera.objects.all()
    data = {
        'alumnos': alumnos,
        'carreras': carreras
    }
    return render(request, 'alumnos.html',data)

def eliminar(request,id):
    victima = Alumno.objects.get(id=id)
    victima.delete()
    return redirect('/loginAlumnos/Alumnos/')

def agregar(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    correo = request.POST['correo']
    contraseña = request.POST['contraseña']
    carrera = request.POST['carrera']
    try:
        imagen = request.FILES['imagen']
    except:
        imagen = 'alumnos/usuario.png'
    alumno = Alumno.objects.create(rut= rut, nombre= nombre, apellidos= apellidos, correo= correo, carrera_id= carrera, contraseña= contraseña, imagen=imagen)
    return redirect('/loginAlumnos/Alumnos/')

def editar(request,id):
    alumno = Alumno.objects.get(id=id)
    carrera = Carrera.objects.all()
    data = {
        'titulo':'Modificando Alumno/Carrera',
        'alumno':alumno,
        'carreras':carrera
    }
    # renderizar el nuevo formulario para modificar (template)
    return render(request,'editarAlumno.html',data)

def editarAlumno(request):
    # rescatar los valores del formulario para pasarlos al objeto 
    # y actualizar sus atributos
    id = request.POST['id']
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    correo = request.POST['correo']
    imagen = request.FILES['imagen']
    carrera = request.POST['carrera']
    contraseña = request.POST['contraseña']
    # buscar el objeto para actualizar
    alumno = Alumno.objects.get(id=id)
    # actualizamos el objeto encontrado
    alumno.rut = rut
    alumno.nombre = nombre
    alumno.apellidos = apellidos
    alumno.correo = correo
    alumno.imagen = imagen
    alumno.carrera_id = carrera
    alumno.contraseña = contraseña
    # Confirmamos el cambio en la base de datos
    alumno.save()
    # redireccionamos al listado en la tabla
    return redirect('/loginAlumnos/Alumnos/')

def alumnosVista(request):
    alumnos = Alumno.objects.all()
    data = {'alumnos':list(alumnos.values('nombre','correo'))}
    return JsonResponse(data)

def usuariosTodos(request):
    encargados = Encargado.objects.all()
    usuarios = Usuario.objects.all()

    data = {
        'encargados':encargados,
        'usuarios':usuarios
    }
    return render(request,'usuarios.html',data)

def eliminarUsuario(request,id):
    victima = Usuario.objects.get(id=id)
    victima.delete()
    return redirect('/loginUsuario/usuarios/')

def agregarUsuario(request):
    nombre_usuario = request.POST['nombre_usuario']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    try:
        imagen = request.FILES['imagen']
    except:
        imagen = 'usuarios/usuario.png'
    encargado = request.POST['encargado']

    usuario = Usuario.objects.create(nombre_usuario=nombre_usuario,contraseña=contraseña,
            correo=correo,imagen=imagen,encargado_id=encargado)
    
    return redirect('/loginUsuario/usuarios/')

def editarEncargado(request,id):
    usuario = Usuario.objects.get(id=id)
    encargados = Encargado.objects.all()
    data = {
        'titulo':'Modificando Usuario',
        'usuario':usuario,
        'encargados':encargados
    }
    # renderizar el nuevo formulario para modificar (template)
    return render(request,'editarUsuario.html',data)

def editarUsuario(request):
    # rescatar los valores del formulario para pasarlos al objeto 
    # y actualizar sus atributos
    id = request.POST['id']
    nombre_usuario = request.POST['nombre_usuario']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    imagen = request.FILES['imagen']
    encargado = request.POST['encargado']
    # buscar el objeto para actualizar
    usuario = Usuario.objects.get(id=id)
    # actualizamos el objeto encontrado
    usuario.id = id
    usuario.nombre_usuario = nombre_usuario
    usuario.contraseña = contraseña
    usuario.correo = correo
    usuario.imagen = imagen
    usuario.encargado_id = encargado
    usuario.save()
    # redireccionamos al listado en la tabla
    return redirect('/loginUsuario/usuarios/')

def usuarioVista(request):
    usuario = Usuario.objects.all()
    data = {'usuario':list(usuario.values('nombre_usuario','correo'))}
    return JsonResponse(data)

def solicitudAlumno(request):
    return render(request, 'solicitudAlumno.html')

def agregarSolicitud(request):
    fecha_solicitud = request.POST['fecha_solicitud']
    deporte = request.POST['deporte']
    print(alumnoid['id'])
    solicitud = Solicitud.objects.create(fecha_solicitud= fecha_solicitud, deporte=deporte,alumno_id=alumnoid['id'])
    return redirect('/solicitudAlumno/')

class AlumnoListado(APIView):
    def get(self,request):
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializar(alumnos,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = AlumnoSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class alumno_detalle(APIView):
    def get_object(self,pk):
        try:
            return Alumno.objects.get(pk=pk)
        except Alumno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializar(alumno)
        return Response(serializer.data)
    def put(self,request,pk):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializar(alumno,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        alumno = self.get_object(pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
