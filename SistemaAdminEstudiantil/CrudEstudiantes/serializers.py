from rest_framework import serializers
from CrudEstudiantes.models import Cursos
from CrudEstudiantes.models import Direcciones
from CrudEstudiantes.models import Estudiantes

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cursos
        fields=['id','nombre','duracion','costo']

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Direcciones
        fields=['id','direccion']

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiantes
        fields=['id','nombre','apellido','num_documento','num_telefono','correo','id_curso','id_direcciones']
