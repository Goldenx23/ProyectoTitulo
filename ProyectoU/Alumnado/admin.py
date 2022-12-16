from django.contrib import admin
from .models import Alumno, Carrera
# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellidos','carrera','correo','contraseña']

class CarreraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'carrera_id']

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Carrera, CarreraAdmin)

