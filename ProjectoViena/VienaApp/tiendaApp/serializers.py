from rest_framework import serializers
from .models import Comanda, DetalleComanda, Productos
from django.shortcuts import get_object_or_404

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nombre', 'precio']

class DetalleComandaSerializer(serializers.ModelSerializer):
    producto_id = serializers.IntegerField(write_only=True)  # Añadido para la creación

    class Meta:
        model = DetalleComanda
        fields = ['producto_id', 'cantidad'] # Añadido 'producto_id' para la creación

    def create(self, validated_data):
        # Obtener el producto basado en el producto_id proporcionado
        producto_id = validated_data.get('producto_id')
        producto = get_object_or_404(Productos, pk=producto_id)
        # Crear el DetalleComanda con el producto recuperado
        detalle_comanda = DetalleComanda.objects.create(producto=producto, **validated_data)
        return detalle_comanda

class ComandaSerializer(serializers.ModelSerializer):
    detallecomanda_set = DetalleComandaSerializer(many=True)

    class Meta:
        model = Comanda
        fields = ['id', 'detallecomanda_set']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detallecomanda_set')
        comanda = Comanda.objects.create(**validated_data)
        for detalle_data in detalles_data:
            # Aquí, `detalle_data` es un diccionario que incluye 'producto_id' y 'cantidad'
            DetalleComanda.objects.create(comanda=comanda, **detalle_data)
        return comanda