from rest_framework.views import APIView
from rest_framework import generics
from .models import Producto, Proveedor, Sector
from .serializers import ProductoSerializer, ProveedorSerializer, SectorSerializers
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
        if not proveedor_id:
            return Response({"error": "No se proporcionó ID de proveedor."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            proveedor_id = int(proveedor_id)
        except ValueError:
            return Response({"error": "El ID no es numerico."}, status=status.HTTP_400_BAD_REQUEST)

        query = """
            SELECT p.* FROM Market_producto p
            INNER JOIN Market_proveedor pv ON pv.id = p.proveedor_id
            WHERE pv.id = %s
        """
        productos = Producto.objects.raw(query, [proveedor_id])
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
