from django.db import models

# Create your models here.
class Cursos(models.Model):
    cod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    duracion = models.CharField(max_length=100, blank=False, null=False)
    costo = models.IntegerField(blank=False, null=False)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_fin = models.DateField(blank=False, null=False)

class Direcciones(models.Model):
    cod = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    barrio = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)

class Estudiantes(models.Model):
    cod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    num_documento = models.BigIntegerField()
    num_telefono = models.BigIntegerField()
    correo = models.EmailField()
    genero = models.CharField(max_length=12, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    cod_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=False)
    cod_direcciones = models.ForeignKey(Direcciones, on_delete=models.CASCADE, null=False)



