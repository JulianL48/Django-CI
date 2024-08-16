import pytest
import datetime
import pytz
from django.utils import timezone
from Market.models import Producto, Proveedor, Sector, Cliente, Factura

@pytest.fixture
def create_clientes(db):
    # Creación de clientes
    cliente1 = Cliente.objects.create(nombre="C1", direccion="Dir1", telefono=3115234564, email="prueba@hotmail.com")
    cliente2 = Cliente.objects.create(nombre="C2", direccion="Dir2", telefono=3115234534, email="prueba1@hotmail.com")
    cliente3 = Cliente.objects.create(nombre="C3", direccion="Dir3", telefono=3115234594, email="prueba2@hotmail.com")
    return [cliente1, cliente2, cliente3]

@pytest.fixture
def create_factura(create_clientes):
    c1, c2, c3 = create_clientes
    tz = pytz.UTC
    # Crear fechas conscientes de la zona horaria
    fecha_emision = timezone.make_aware(datetime.datetime(2024, 8, 16, 0, 0, 0), tz)
    fecha_vencimiento1 = timezone.make_aware(datetime.datetime(2024, 9, 16, 0, 0, 0), tz)
    fecha_vencimiento2 = timezone.make_aware(datetime.datetime(2024, 8, 26, 0, 0, 0), tz)
    fecha_vencimiento3 = timezone.make_aware(datetime.datetime(2024, 10, 16, 0, 0, 0), tz)
    # Creación de facturas
    factura1 = Factura.objects.create(cliente_id=c1, fecha_emision=fecha_emision, fecha_vencimiento=fecha_vencimiento1, total=0)
    factura2 = Factura.objects.create(cliente_id=c2, fecha_emision=fecha_emision, fecha_vencimiento=fecha_vencimiento2, total=0)
    factura3 = Factura.objects.create(cliente_id=c3, fecha_emision=fecha_emision, fecha_vencimiento=fecha_vencimiento3, total=0)
    return [factura1, factura2, factura3]

@pytest.fixture
def create_sectors(db):
    # Creación de sectores
    sector_p = Sector.objects.create(nombre="Primario", caracteristica="SP")
    sector_s = Sector.objects.create(nombre="Secundario", caracteristica="SS")
    sector_t = Sector.objects.create(nombre="Terciario", caracteristica="ST")
    return [sector_p, sector_s, sector_t]

@pytest.fixture
def create_proveedors(create_sectors):
    sector_p, sector_s, sector_t = create_sectors
    # Creación de proveedores
    prov_1 = Proveedor.objects.create(nombre="Proveedor 1", nit="1818182", sector_fk=sector_p)
    prov_2 = Proveedor.objects.create(nombre="Proveedor 2", nit="1818182", sector_fk=sector_s)
    prov_3 = Proveedor.objects.create(nombre="Proveedor 3", nit="1818182", sector_fk=sector_t)
    return [prov_1, prov_2, prov_3]

@pytest.fixture
def create_products(create_proveedors):
    prov_1, prov_2, prov_3 = create_proveedors
    # Crear productos necesarios para la prueba
    Producto.objects.create(nombre="P1", descripcion="Desc1", precio=6000, creado="2022-02-19", proveedor=prov_1)
    Producto.objects.create(nombre="P2", descripcion="Desc2", precio=2000, creado="2022-03-15", proveedor=prov_2)
    Producto.objects.create(nombre="P3", descripcion="Desc3", precio=10000, creado="2022-01-20", proveedor=prov_2)
    Producto.objects.create(nombre="P4", descripcion="Desc4", precio=5500, creado="2022-04-17", proveedor=prov_3)
