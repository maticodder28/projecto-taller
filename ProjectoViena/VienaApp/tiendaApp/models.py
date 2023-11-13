from django.db import models
from django.utils import timezone
from tiendaApp.choices import *

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return "{} {} ".format( self.nombre, self.descripcion)
    
    class Meta:
        verbose_name = "TipoUsuario"
        verbose_name_plural = "TipoUsuarios"
        ordering = ["nombre", "descripcion"]

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=EstadoUsuario, default='Activo')

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format( self.nombre, self.apellido, self.rut, self.email, self.password, self.password2, self.telefono, self.tipoUsuario, self.estado)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["nombre", "apellido", "rut", "email", "password", "password2", "telefono" , "tipoUsuario", "estado"]

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)


    def __str__(self):
        return "{} {} {} {} {}".format(self.nombre, self.descripcion, self.precio, self.categoria, self.imagen)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre", "descripcion", "precio", "categoria", "imagen"]



class Mesas(models.Model):
    numero = models.IntegerField()
    estado = models.CharField(max_length=50, choices=EstadoMesa, default='Libre')

    def __str__(self):
        return "{} {}".format( self.numero, self.estado)
    
    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"
        ordering = ["numero", "estado"]

class Comanda(models.Model):
    fecha = models.DateField()
    productos = models.ManyToManyField(Productos, through='DetalleComanda')
    estado = models.CharField(max_length=50, choices=EstadoPedido, default='Pendiente')

    def __str__(self):
            # Inicializa una lista vacía para almacenar los nombres de los productos
            productos_str = []

            # Itera sobre todos los productos relacionados con esta comanda
            for producto in self.productos.all():
                # Añade el nombre del producto a la lista
                productos_str.append(str(producto.nombre))

            # Une los nombres de los productos en una sola cadena separada por comas
            productos_juntos = ', '.join(productos_str)

            # Devuelve una representación en cadena que incluye la fecha, el estado y los productos
            return "Comanda del {} ({})".format(self.fecha, productos_juntos)
    
    class Meta:
        verbose_name = "Comanda"
        verbose_name_plural = "Comandas"
        ordering = ["fecha"]

class DetalleComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format( self.comanda, self.producto, self.cantidad)
    
    class Meta:
        verbose_name = "DetalleComanda"
        verbose_name_plural = "DetalleComandas"
        ordering = ["comanda", "producto", "cantidad"]

