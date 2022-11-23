from django.shortcuts import render, redirect
from .models import Solicitud, Id, Alumno
# Create your views here.
def index(request):
    return render(request,'index.html')

def SolicitudTodas(request):
    Solicitudes = Solicitud.objects.all()
    Ids = Id.objects.all()
    Alumnos = Alumno.objects.all()
    data = {
        'Solicitudes': Solicitud,
        'Ids': Id,
        'Alumnos': Alumno
    }
    return render(request, 'Alumnos.html')

def eliminar(request,id):
    victima = Solicitud.objects.get(id=id)
    victima.delete()
    return redirect('/alumnos/')

def agregar(request):
    # rescatamos los values a través de los name del formulario 
    # para luego usarlos como atributos del nuevo objeto empleado
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    fechaNac = request.POST['fechaNac']
    cargo = request.POST['cargo']
    departamento = request.POST['departamento']
    try:
        foto = request.FILES['foto']
    except:
        foto = 'empleados/empleado.png'
    # Creamos el objeto en el modelo, que es lo mismo
    #  (ORM) que crear un registro en la tabla
    empleado = Solicitud.objects.create(rut=rut,nombre=nombre,apellidos=apellidos,
        fechaNac=fechaNac,cargo_id=cargo,departamento_id=departamento,foto=foto)
    
    return redirect('/empleados/')

def editar(request,id):
    # buscar el empleado a modificar
    empleado = Solicitud.objects.get(id=id)
    # cargar la data
    cargos = Alumno.objects.all()
    deptos = Id.objects.all()
    data = {
        'titulo':'Modificando Solicitud',
        'Alumno':Alumno,
        'SOlicitud':Solicitud,
        'idSolicitud':Id,
    }
    # renderizar el nuevo formulario para modificar (template)
    return render(request,'editarSolicitud.html',data)

def editarEmpleado(request):
    # rescatar los valores del formulario para pasarlos al objeto 
    # y actualizar sus atributos
    id = request.POST['id']
    run = request.POST['run']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    fechaNac = request.POST['fechaNac']
    foto = request.FILES['foto']
    # buscar el objeto para actualizar
    Alumno = Alumno.objects.get(id=id)
    # actualizamos el objeto encontrado
    Alumno.rut = rut
    Alumno.nombre = nombre
    Alumno.apellidos = apellidos
    Alumno.fechaNac = fechaNac
    Alumno.departamento_id = departamento
    Alumno.foto = foto
    # Confirmamos el cambio en la base de datos
    Alumno.save()
    # redireccionamos al listado en la tabla
    return redirect('/empleados/')


