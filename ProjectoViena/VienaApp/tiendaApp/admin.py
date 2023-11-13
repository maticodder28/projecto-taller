from django.contrib import admin
from django.contrib.admin import ModelAdmin  # Agrega esta línea

# Register your models here.
from tiendaApp.models import TipoUsuario, Usuarios, Productos, Mesas, Comanda, DetalleComanda, Categoria

class TipoUsuarioAdmin(ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion' )

class UsuariosAdmin(ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'email', 'password', 'password2', 'telefono', 'tipoUsuario', 'estado')
    search_fields = ('nombre', 'apellido', 'rut', 'email', 'password', 'password2', 'telefono', 'tipoUsuario', 'estado')

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

admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Mesas, MesasAdmin)
admin.site.register(Comanda, ComandaAdmin)
admin.site.register(DetalleComanda, DetalleComandaAdmin)
admin.site.register(Categoria, CategoriaAdmin)