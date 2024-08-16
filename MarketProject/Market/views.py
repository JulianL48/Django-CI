from django.utils import timezone
from django.db import transaction
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework import generics
from .models import Producto, Proveedor, Sector, Cliente, Factura, Detalle_Factura
from .serializers import ProductoSerializer, ProveedorSerializer, SectorSerializers, ClienteSerializer, FacturaSerializer, Detalle_FacturaSerializer
from rest_framework.response import Response
from rest_framework import status

class SectorListCreate(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializers

class SectorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializers

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FacturaListCreate(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaListCreate(generics.ListCreateAPIView):
    queryset = Detalle_Factura.objects.all()
    serializer_class = Detalle_FacturaSerializer

class DetalleFacturaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalle_Factura.objects.all()
    serializer_class = Detalle_FacturaSerializer
            
#Consulta todos los productos cuyo precio sea mayr a 5000
class ProductosMayorQue5000(APIView):
    def get(self, request):
        productos = Producto.objects.filter(precio__gt=5000)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#Consulta todos los productos cuyo proveedor sea parmalat
class ProductosPorProveedor(APIView):
    def post(self, request):
        proveedor_id = request.data.get('proveedor_id')
        query = """
            SELECT p.* FROM Market_producto p
            INNER JOIN Market_proveedor pv ON pv.id = p.proveedor_id
            WHERE pv.id = %s
        """
        productos = Producto.objects.raw(query, [proveedor_id])
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Facturando(APIView):
    @transaction.atomic
    def post(self, request):
        client_id = request.data.get('cliente_id')
        products = request.data.get('productos')

        try:
            client = Cliente.objects.get(id=client_id)
            # Creamos la factura
            factura = Factura.objects.create(
                cliente_id=client,
                fecha_emision=timezone.now(),
                fecha_vencimiento=timezone.now().date() + timedelta(days=30),  # Suponiendo vencimiento en 30 días
                total=0
            )
            total_final=0;
            for product in products:
                product_id = product.get('id_producto')
                cantidad = product.get('cantidad')
                try:
                    producto = Producto.objects.get(id=product_id)
                    precio_unitario = producto.precio
                    subtotal = cantidad * precio_unitario
                    total_final += subtotal
                    # Crear el detalle de la factura
                    Detalle_Factura.objects.create(
                        factura_id=factura,
                        producto_id=producto,
                        cantidad=cantidad,
                        precio_unitario=precio_unitario,
                        subtotal=subtotal
                    )
                    # Actualizar el total de la factura
                    factura.total = total_final
                    factura.save()
                    
                except Producto.DoesNotExist:
                    return Response(f"Producto con id {product_id} no encontrado", status=status.HTTP_404_NOT_FOUND)
                
            if factura.total>0 :
                response_data = {
                        "factura_id": factura.id,
                        "mensaje": "Factura generada correctamente"
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else :
                return Response("Ocurrio un error al generar el total de la factura", status=status.HTTP_400_BAD_REQUEST)
        except Cliente.DoesNotExist:
            raise ValueError("Cliente no encontrado")
