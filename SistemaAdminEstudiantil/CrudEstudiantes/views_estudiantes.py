#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from CrudEstudiantes.models import Estudiantes
from CrudEstudiantes.serializers import EstudiantesSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
############################
##METODOS PARA DIRECCIONES##
############################

#Consultar estudiantes
@api_view(['GET', 'POST'])
def MetEstudiantes(request):

    if request.method == 'GET':
        est = Estudiantes.objects.all()
        serializer=EstudiantesSerializer(est,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar direcciones
    elif request.method == 'POST':  
        serializer = EstudiantesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#buscar, actualizar, eliminar estudiantes, se hace por el id del estudiante
@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detail(request,key):
    try:
        est = Estudiantes.objects.get(pk=key)
    except Estudiantes.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstudiantesSerializer(est)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EstudiantesSerializer(est, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        est.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)