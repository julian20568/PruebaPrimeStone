from rest_framework import serializers
from CrudEstudiantes.models import Cursos
from CrudEstudiantes.models import Direcciones
from CrudEstudiantes.models import Estudiantes

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cursos
        fields=['cod','nombre','duracion','costo','fecha_inicio','fecha_fin']

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Direcciones
        fields=['cod','pais','ciudad','barrio','direccion']

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiantes
        fields=['cod','nombre','apellido','num_documento','num_telefono','correo','genero','fecha_nacimiento','cod_curso','cod_direcciones']
