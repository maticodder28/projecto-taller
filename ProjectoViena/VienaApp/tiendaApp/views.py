from django.shortcuts import render, redirect, get_object_or_404
from tiendaApp.forms import ProductoForm, RegistroUsuarioForm
from tiendaApp.models import Productos, Categoria, Usuarios
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

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
    productos = Producto.objects.filter(categoria_id=categoria_id)
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

@staff_member_required
def registro_usuario(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = RegistroUsuarioForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('inicio')  # Redirige a donde necesites
    else:
        user_form = UserCreationForm()
        profile_form = RegistroUsuarioForm()
    return render(request, 'registro_usuario.html', {'user_form': user_form, 'profile_form': profile_form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)  # Esta línea efectivamente cierra la sesión del usuario
    return redirect('login')  # Redirige al usuario a la página de inicio de sesión