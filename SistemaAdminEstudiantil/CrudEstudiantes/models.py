from django.db import models

# Create your models here.
class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    duracion = models.CharField(max_length=100, blank=False, null=False)
    costo = models.IntegerField(blank=False, null=False)

class Direcciones(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100, blank=False, null=False)

class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    num_documento = models.IntegerField(blank=False, null=False)
    num_telefono = models.IntegerField(blank=False, null=False)
    correo = models.EmailField()
    id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=False)
    id_direcciones = models.ForeignKey(Direcciones, on_delete=models.CASCADE, null=False)


