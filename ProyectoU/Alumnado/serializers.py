from rest_framework import serializers
from .models import Alumno
class AlumnoSerializar(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
