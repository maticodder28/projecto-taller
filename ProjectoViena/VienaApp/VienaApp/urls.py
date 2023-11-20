"""
URL configuration for VienaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from tiendaApp import views as vistas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas.base, name='base'),
    path('inicio/', vistas.inicio, name='inicio'),
    path('agregarproducto/', vistas.ingresoproducto, name='ingresoproducto'),
    path('listaproductos/', vistas.listaproductos, name='listaproductos'),
    path('categoria/<int:categoria_id>/', vistas.productos_por_categoria, name='productos_por_categoria'),
    path('categoria/<int:categoria_id>/', vistas.detalles_categoria, name='categoria_detalles'),
    path('producto/<int:producto_id>/', vistas.producto_detalle, name='producto_detalle'),
    path('producto/editar/<int:producto_id>/', vistas.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', vistas.eliminar_producto, name='eliminar_producto'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("registro/", vistas.register_request, name="registro"),
    path("comandas/", vistas.crear_comanda, name="crear_comanda"),
    path('cocina/', vistas.vista_cocina, name='vista_cocina'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)