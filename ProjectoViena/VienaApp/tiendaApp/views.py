from django.shortcuts import render, redirect, get_object_or_404
from tiendaApp.forms import ProductoForm, NewUserForm, DetalleComandaForm
from tiendaApp.models import Productos, Categoria, Comanda, DetalleComanda
from django.db.models import Q
from django.contrib.auth import login
from django.contrib import messages
import json
from django.http import JsonResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')

def inicio(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'inicio.html', {'categorias': categorias})


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
    # Obtén el objeto del producto o muestra un error 404 si no existe
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
    if request.method == 'POST':
        data = json.loads(request.body)
        productos_data = data.get('productos')

        comanda = Comanda.objects.create()

        for item in productos_data:
            producto_id = item['producto_id']
            cantidad = item['cantidad']

            producto = Productos.objects.get(id=producto_id)
            DetalleComanda.objects.create(comanda=comanda, producto=producto, cantidad=cantidad)

        return JsonResponse({'success': True})

    productos = Productos.objects.all()
    return render(request, 'crear_comanda.html', {'productos': productos})


def vista_cocina(request):
    comandas = Comanda.objects.all().order_by('fecha_creacion')
    return render(request, 'vista_cocina.html', {'comandas': comandas})