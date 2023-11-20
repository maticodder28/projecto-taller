from django.contrib import admin
from django.contrib.admin import ModelAdmin  # Agrega esta línea

# Register your models here.
from tiendaApp.models import Productos, Mesas, Comanda, DetalleComanda, Categoria, UserProfile
from django.contrib.auth.models import User, Group



class ProductosAdmin(ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria', 'imagen')
    search_fields = ('nombre', 'descripcion', 'precio', 'categoria', 'imagen')

class MesasAdmin(ModelAdmin):
    search_fields = ('numero', 'estado')

class ComandaAdmin(ModelAdmin):
    search_fields = ('fecha', 'mesa', 'usuario')

class DetalleComandaAdmin(ModelAdmin):
    list_display = ('comanda', 'producto', 'cantidad')
    search_fields = ('comanda', 'producto', 'cantidad')

class CategoriaAdmin(ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen')
    search_fields = ('nombre', 'descripcion', 'imagen')

class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'nombre', 'apellido', 'cargo', 'rut')
    search_fields = ('user', 'nombre', 'apellido', 'cargo', 'rut')
    
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Mesas, MesasAdmin)
admin.site.register(Comanda, ComandaAdmin)
admin.site.register(DetalleComanda, DetalleComandaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)