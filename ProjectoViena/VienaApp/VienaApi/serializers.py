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
    usuario_asignado = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comanda
        fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detallecomanda_set', [])
        comanda = Comanda.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetalleComanda.objects.create(comanda=comanda, **detalle_data)
        return comanda
    
    def save(self, **kwargs):
        kwargs['usuario_asignado'] = self.context['request'].user
        return super().save(**kwargs)