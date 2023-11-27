from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from tiendaApp.forms import ProductoForm, NewUserForm, DetalleComandaForm
from tiendaApp.models import Productos, Categoria, Comanda, DetalleComanda
from django.db.models import Q
from django.contrib.auth import login
from django.contrib import messages
import json
from django.http import JsonResponse
from openpyxl import Workbook
import datetime
from django.http import HttpResponse
from django.utils.timezone import make_naive, get_default_timezone, is_naive
from collections import Counter
from django.conf import settings
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tiendaApp.serializers import ComandaSerializer
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

# Create your views here.
def base(request):
    return render(request, 'base.html')

def modificar(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'modificar.html', {'categorias': categorias})


def ingresoproducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaproductos')
    else:
        form = ProductoForm()
    return render(request, 'ingresoproducto.html', {'form': form})


def listaproductos(request):
    query = request.GET.get('q')
    productos = Productos.objects.all()

    if query:
        # Filtra los productos que contienen la consulta en el nombre o la descripción
        productos = productos.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))

    return render(request, 'listaproductos.html', {'productos': productos, 'query': query})

def productos_por_categoria(request, categoria_id):
    productos = Productos.objects.filter(categoria_id=categoria_id)
    categoria = Categoria.objects.get(id=categoria_id)
    return render(request, 'productos_por_categoria.html', {'productos': productos, 'categoria': categoria})

def detalles_categoria(request, categoria_id):
    productos = Productos.objects.filter(categoria_id=categoria_id)
    return render(request, 'detalles_categoria.html', {'productos': productos})

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # Redirigir a donde sea necesario después de actualizar
            return redirect('listaproductos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto_detalle.html', {'form': form, 'producto': producto})
    
def editar_producto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_detalle', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    # Obtiene el objeto del producto o muestra un error 404 si no existe
    producto = get_object_or_404(Productos, id=producto_id)
    
    if request.method == 'POST':
        # Si la solicitud es POST, elimina el producto
        producto.delete()
        # Redirige a la página de inicio o a donde desees después de la eliminación
        return redirect('inicio')
    
    # Renderiza una página de confirmación de eliminación (puedes crearla si lo deseas)
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso." )
            return redirect("inicio")  # Redirecciona a la página de inicio
        messages.error(request, "Registro no exitoso. Información inválida.")
    form = NewUserForm()
    return render(request=request, template_name="registration/registro.html", context={"register_form":form})

def crear_comanda(request):
    comestibles = Productos.objects.filter(categoria=1)  # ID para Comestibles
    bebestibles = Productos.objects.filter(categoria=2)  # ID para Bebestibles
    bebidasalcoholicas = Productos.objects.filter(categoria=3)  # ID para Bebidas Alcohólicas
    
    return render(request, 'crear_comanda.html', {
        'comestibles': comestibles,
        'bebestibles': bebestibles,
        'bebidasalcoholicas': bebidasalcoholicas
    })

def vista_cocina(request):
    comandas = Comanda.objects.prefetch_related('detallecomanda_set').all().order_by('fecha_creacion')
    return render(request, 'vista_cocina.html', {'comandas': comandas})

def generar_informe_ventas(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Convertir las fechas de string a objetos datetime
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()

        # Crear un libro de trabajo de Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Informe de Ventas"

        # Añadir encabezados a la hoja de Excel
        columnas = ['ID Comanda', 'Fecha', 'Total']
        ws.append(columnas)

        # Filtrar comandas por el rango de fechas
        comandas = Comanda.objects.filter(fecha_creacion__range=[fecha_inicio, fecha_fin])

        # Añadir datos de comandas a la hoja
        for comanda in comandas:
            # Convertir la fecha a zona horaria neutral
            fecha_sin_tz = make_naive(comanda.fecha_creacion)
            ws.append([comanda.id, fecha_sin_tz, comanda.total])

        # Configurar la respuesta para descargar el archivo de Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')
        nombre_archivo = f"Informe_Ventas_{fecha_inicio}_{fecha_fin}.xlsx"
        response['Content-Disposition'] = f'attachment; filename={nombre_archivo}'

        # Guardar el libro de trabajo en la respuesta
        wb.save(response)

        return response

    # Si no es un POST, renderizar el formulario
    return render(request, 'generar_informe.html')

def informe_producto(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Convertir las fechas de string a objetos datetime
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')

        # Verifica si las fechas son naive y, si no, conviértelas
        if not is_naive(fecha_inicio):
            fecha_inicio = make_naive(fecha_inicio, get_default_timezone())
        if not is_naive(fecha_fin):
            fecha_fin = make_naive(fecha_fin, get_default_timezone())

        # Obtener todas las comandas en el rango de fechas
        comandas = Comanda.objects.filter(fecha_creacion__range=[fecha_inicio, fecha_fin])

        # Contabilizar los productos vendidos
        contador_productos = Counter()
        for comanda in comandas:
            for detalle in comanda.detallecomanda_set.all():
                contador_productos[detalle.producto] += detalle.cantidad

        # Crear un libro de trabajo de Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Productos Vendidos"

        # Crear un libro de trabajo de Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Productos Vendidos"

        # Añadir encabezados a la hoja de Excel
        ws.append(['Producto', 'Descripción', 'Precio', 'Cantidad Vendida', 'Total'])

        # Añadir datos de los productos vendidos
        for producto, cantidad in contador_productos.most_common():
            total = producto.precio * cantidad
            ws.append([
                producto.nombre, 
                producto.descripcion, 
                producto.precio, 
                cantidad,
                total  # Total calculado
            ])

        # Configurar la respuesta para descargar el archivo de Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')
        nombre_archivo = f"Productos_Vendidos_{fecha_inicio}_{fecha_fin}.xlsx"
        response['Content-Disposition'] = f'attachment; filename={nombre_archivo}'

        # Guardar el libro de trabajo en la respuesta
        wb.save(response)

        return response

    # Si no es un POST, renderizar el formulario
    return render(request, 'informe_producto.html')

def seleccionar_informes(request):
    return render(request, 'seleccionar_informes.html')

def confirmar_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    detalles_comanda = comanda.detallecomanda_set.all()  # Asumiendo que tienes un related_name configurado

    total_comanda = sum(detalle.subtotal for detalle in detalles_comanda)

    return render(request, 'confirmar_comanda.html', {
        'comanda': comanda,
        'detalles_comanda': detalles_comanda,
        'total_comanda': total_comanda
    })


def comanda_exitosa(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    detalles_comanda = comanda.detallecomanda_set.all()
    total_comanda = sum(detalle.subtotal for detalle in detalles_comanda)

    return render(request, 'comanda_exitosa.html', {
        'comanda': comanda,
        'detalles_comanda': detalles_comanda,
        'total_comanda': total_comanda
    })

class CrearComandaAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ComandaSerializer(data=request.data)
        if serializer.is_valid():
            comanda = serializer.save()
            return Response({'comanda_id': comanda.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def confirmar_comanda_api(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    comanda.confirmada = True  # Asumiendo que tienes un campo así
    comanda.save()
    return Response({'success': True})

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)