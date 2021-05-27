#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from CrudEstudiantes.models import Direcciones
from CrudEstudiantes.serializers import DireccionesSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
############################
##METODOS PARA DIRECCIONES##
############################

#Consultar direcciones
@api_view(['GET', 'POST'])
def MetDirecciones(request):

    if request.method == 'GET':
        dir=Direcciones.objects.all()
        serializer=DireccionesSerializer(dir,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar direcciones
    elif request.method == 'POST':  
        serializer = DireccionesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#buscar, actualizar, eliminar cursos, se hace por el id del curso
@api_view(['GET', 'PUT', 'DELETE'])
def direcciones_detail(request,key):
    try:
        direc = Direcciones.objects.get(pk=key)
    except Direcciones.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DireccionesSerializer(direc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DireccionesSerializer(direc, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        direc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de direcciones por pais
@api_view(['GET'])
def Dir_pais(request,ps):
    try:
        pais = Direcciones.objects.get(pais=ps)
    except Direcciones.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DireccionesSerializer(pais)
        return JsonResponse(serializer.data)

#consulta de direcciones por ciudad
@api_view(['GET'])
def Dir_ciudad(request,ciu):
    try:
        ciu = Direcciones.objects.get(ciudad=ciu)
    except Direcciones.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DireccionesSerializer(ciu)
        return JsonResponse(serializer.data)

#consulta de direcciones por barrio
@api_view(['GET'])
def Dir_barrio(request,bar):
    try:
        bar = Direcciones.objects.get(barrio=bar)
    except Direcciones.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DireccionesSerializer(bar)
        return JsonResponse(serializer.data)
