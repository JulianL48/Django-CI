from rest_framework import serializers
from .models import Producto, Proveedor, Sector, Cliente, Factura, Detalle_Factura

class SectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Factura
        fields = '__all__'