from django.db import models
from django.utils import timezone
from tiendaApp.choices import *
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)  # Cargo
    rut = models.CharField(max_length=12)  # Asegúrate de validar este campo correctamente

    # Agrega cualquier otro campo que necesites

    def __str__(self):
        return self.user.username

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

    def __str__(self):
        return "{} {}".format( self.numero)
    
    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"
        ordering = ["numero"]

class Comanda(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Productos, through='DetalleComanda')
    usuario_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comandas_asignadas')
    # Otros campos...

    def __str__(self):
        return f"Comanda {self.id} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.detallecomanda_set.all())

class DetalleComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"

    @property
    def subtotal(self):
        return self.cantidad * self.producto.precio

