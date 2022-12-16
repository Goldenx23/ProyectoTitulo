from django.db import models
import os
from django.utils import timezone
from datetime import datetime

class Carrera(models.Model):
    nombre = models.CharField(max_length = 100,verbose_name = 'Nombre de carrera')
    carrera_id = models.BigAutoField(primary_key = True, verbose_name='Carrera id')

    def __str__(self):
        return "{}".format(self.nombre)
    
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        db_table = 'carrera'

class Alumno(models.Model):
    rut = models.CharField(max_length= 12, verbose_name = 'RUT')
    nombre = models.CharField(max_length= 100, verbose_name= 'Nombre' )
    apellidos = models.CharField(max_length= 100, verbose_name= 'Apellidos')
    correo = models.CharField(max_length= 100, verbose_name= 'Correo')
    contraseña = models.CharField(max_length= 100, verbose_name= 'Contraseña', blank= False, default= 0, null= True)
    #--Relación--
    carrera = models.ForeignKey(Carrera,on_delete = models.RESTRICT)

    def generaNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'alumnos'
        fecha = datetime.now().strftime("%d%m%Y_%H%M%S")  # d=dia;m=mes;Y=año_H=hora;M=minutos;S=segundos
        nombre = "{}.{}".format(fecha,extension)
        return os.path.join(ruta,nombre)
    imagen = models.ImageField('Imagen', upload_to=generaNombre, null=True, default='alumnos/alumno.png')    

    def __str__(self):
        return "{} {}".format(self.rut, self.nombre, self.apellidos, self.correo, self.contraseña)
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        db_table = 'alumno'
        ordering = ['rut','nombre', 'apellidos','correo','contraseña']
    

class Encargado(models.Model):
    rut = models.CharField(verbose_name='RUT Encargado',max_length=10)
    nombre = models.CharField(verbose_name='Nombre Encargado',max_length=100)
    sexo = models.CharField(verbose_name='Sexo Encargado',max_length=10)
    fecha_nacimiento = models.DateField(blank=True,null=True,verbose_name='Fecha Nacimiento Encargado')

    def __str__(self):
        return "{} {}".format(self.nombre,self.rut)

    class Meta:
        verbose_name = 'Encargado'
        verbose_name_plural = 'Encargados'
        db_table = 'encargado'
        

class Usuario(models.Model):
    nombre_usuario = models.CharField(verbose_name='Nombre Usuario Encargado',max_length=100)
    contraseña = models.CharField(verbose_name='Contraseña Encargado',max_length=100)
    correo = models.CharField(verbose_name='Correo Encargado',max_length=100)

    def generaNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'usuarios'
        fecha = datetime.now().strftime("%d%m%Y_%H%M%S")  # d=dia;m=mes;Y=año_H=hora;M=minutos;S=segundos
        nombre = "{}.{}".format(fecha,extension)
        return os.path.join(ruta,nombre)

    imagen = models.ImageField('Imagen', upload_to=generaNombre, null=True, default='usuarios/usuario.png')
    encargado = models.ForeignKey(Encargado,on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombre_usuario,self.correo)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

class Solicitud(models.Model):
    estado = models.CharField(verbose_name='Estado Solicitud',max_length=100, default="pendiente")
    fecha_solicitud = models.DateTimeField(verbose_name='Fecha de Solicitud')
    deporte = models.CharField(verbose_name='Deporte', max_length= 20, default= "futbol")
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)

    def _str_(self):
        return "{} {}".format(self.estado,self.fecha_solicitud, self.deporte)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        db_table = 'solicitud'