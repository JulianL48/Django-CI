from django.urls import path
from .views import (
    ProductoListCreate, ProductoRetrieveUpdateDestroy, ProveedorListCreate, ProveedorRetrieveUpdateDestroy, 
    SectorListCreate, SectorRetrieveUpdateDestroy, ProductosMayorQue5000, ProductosPorProveedor, 
    ClienteListCreate, ClienteRetrieveUpdateDestroy, FacturaListCreate, FacturaRetrieveUpdateDestroy, 
    DetalleFacturaListCreate, DetalleFacturaRetrieveUpdateDestroy, Facturando
)

urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-detail'),
    path('proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-detail'),
    path('sectores/', SectorListCreate.as_view(), name='sector-list-create'),
    path('sectores/<int:pk>/', SectorRetrieveUpdateDestroy.as_view(), name='sector-detail'),
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('facturas/', FacturaListCreate.as_view(), name='factura-list-create'),
    path('facturas/<int:pk>/', FacturaRetrieveUpdateDestroy.as_view(), name='factura-detail'),
    path('detalle_facturas/', DetalleFacturaListCreate.as_view(), name='detalleF-list-create'),
    path('detalle_facturas/<int:pk>/', DetalleFacturaRetrieveUpdateDestroy.as_view(), name='detalleF-detail'),
    path('productos/mayorque500/', ProductosMayorQue5000.as_view(), name='productos_mayor_que_5000'),
    path('productos/ByProveedor/', ProductosPorProveedor.as_view(), name='productos_por_proveedor_post'),
    path('facturas/CreateDetalleFactura/', Facturando.as_view(), name='create_detalle_factura'),
]