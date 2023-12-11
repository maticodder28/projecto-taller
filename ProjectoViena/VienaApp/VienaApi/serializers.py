from rest_framework import serializers
from tiendaApp.models import Productos, Categoria, Comanda, DetalleComanda

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class DetalleComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleComanda
        fields = ['producto', 'cantidad']

class ComandaSerializer(serializers.ModelSerializer):
    detallecomanda_set = DetalleComandaSerializer(many=True)

    class Meta:
        model = Comanda
        fields = ['fecha_creacion', 'detallecomanda_set']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detallecomanda_set')
        comanda = Comanda.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetalleComanda.objects.create(comanda=comanda, **detalle_data)
        return comanda