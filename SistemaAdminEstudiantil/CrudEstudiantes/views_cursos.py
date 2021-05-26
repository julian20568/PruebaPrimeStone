#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from CrudEstudiantes.models import Cursos
from CrudEstudiantes.serializers import CursosSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#######################
##METODOS PARA CURSOS##
#######################

#Consultar cursos
@api_view(['GET', 'POST'])
def MetCursos(request):

    if request.method == 'GET':
        Cur=Cursos.objects.all()
        serializer=CursosSerializer(Cur,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar cursos
    elif request.method == 'POST':  
        serializer = CursosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#buscar, actualizar, eliminar cursos, se hace por el id del curso
@api_view(['GET', 'PUT', 'DELETE'])
def cursos_detail(request,key):
    try:
        cursos = Cursos.objects.get(pk=key)
    except Cursos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursosSerializer(cursos)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CursosSerializer(cursos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cursos.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de cursos por nombre
@api_view(['GET'])
def Curso_nombre(request,nom):
    try:
        cursos = Cursos.objects.get(nombre=nom)
    except Cursos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursosSerializer(cursos)
        return JsonResponse(serializer.data)

#consulta de cursos por duración
@api_view(['GET'])
def Curso_duracion(request,dur):
    try:
        cursos = Cursos.objects.get(duracion=dur)
    except Cursos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursosSerializer(cursos)
        return JsonResponse(serializer.data)

#consulta de cursos por costo
@api_view(['GET'])
def Curso_costo(request,cost):
    try:
        cursos = Cursos.objects.get(costo=cost)
    except Cursos.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursosSerializer(cursos)
        return JsonResponse(serializer.data)