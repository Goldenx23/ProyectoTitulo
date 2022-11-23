from django.db import models
from datetime import datetime
from email.policy import default
import os
from django.db import models
from django.utils import timezone

# Create your models here.
class Solicitud(models.Model):
    # verbose_name= indica como se mostrara en un formulario
    # max_length= indica el largo maximo de caracteres
    nombre = models.CharField(verbose_name='Solicitud de fecha',max_length=100)
    # timezone.now = obtiene la fecha y hora del server
    creado = models.DateTimeField(default=timezone.now) 
    fechaSolicitada =  models.DateField(blank=True,null=True,verbose_name='Fecha solicitada')

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'
        db_table = 'fecha'

class Id(models.Model):
    codigo = models.BigAutoField(primary_key=True,verbose_name='Id de solicitud')
    nombre = models.CharField(max_length=100,verbose_name='codigo de la solicitud')
    creado = models.DateTimeField(default=timezone.now)
    # blank=True   permite datos en blanco
    # null=True    permite datos nulos
    eliminado = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Id'
        verbose_name_plural = 'Ids'
        db_table = 'id'

class Alumno(models.Model):
    run = models.CharField(max_length=12,verbose_name='RUT')
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellidos = models.CharField(max_length=100,verbose_name='Apellidos')
    fechaNac = models.DateField(blank=True,null=True,verbose_name='Fecha de nacimiento')
    # ----------- Relaciones --------------------------
    Id = models.ForeignKey(Id,on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now)

    def generaNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'empleados'
        fecha = datetime.now().strftime("%d%m%Y_%H%M%S")  # d=dia;m=mes;Y=año_H=hora;M=minutos;S=segundos
        nombre = "{}.{}".format(fecha,extension)
        return os.path.join(ruta,nombre)

    foto = models.ImageField(upload_to=generaNombre,null=True,default='empleados/empleado.png')

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellidos)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['nombre','apellidos']
