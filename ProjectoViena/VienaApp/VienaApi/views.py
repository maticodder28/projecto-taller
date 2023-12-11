from django.shortcuts import render
from tiendaApp.models import Productos, Categoria, Comanda
from django.http import JsonResponse
from VienaApi.serializers import ProductoSerializer, CategoriaSerializer, ComandaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def productosApi(request):
    productos = Productos.objects.all()
    data = {
        'productos' : list(
            productos.values(
                "id",
                "nombre",
                "descripcion",
                "precio",
                "categoria_id",
                "imagen"
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET'])
def productos_listado(request):
    if request.method == 'GET':
        productos = Productos.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def producto_detalle(request, pk):
    try:
        producto = Productos.objects.get(pk=pk)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def categoriaApi(request):
    categoria = Categoria.objects.all()
    data = {
        'categoria' : list(
            categoria.values(
                "id",
                "nombre",
                "descripcion",
            )
        )
    }
    return JsonResponse(data)

@api_view(['GET'])
def categoria_listado(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detalle(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def crear_comanda(request):
    serializer = ComandaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def comanda_listado(request):
    if request.method == 'GET':
        comandas = Comanda.objects.all()
        serializer = ComandaSerializer(comandas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComandaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comanda_detalle(request, pk):
    try:
        comanda = Comanda.objects.get(pk=pk)
    except Comanda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComandaSerializer(comanda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComandaSerializer(comanda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comanda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)