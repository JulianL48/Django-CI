import pytest
from Market.models import Producto, Proveedor, Sector

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
    Producto.objects.create(nombre="P1", marcas="MP1", precio=6000, creado="2022-02-19", proveedor=prov_1)
    Producto.objects.create(nombre="P2", marcas="MP2", precio=2000, creado="2022-03-15", proveedor=prov_2)
    Producto.objects.create(nombre="P3", marcas="MP3", precio=10000, creado="2022-01-20", proveedor=prov_2)
    Producto.objects.create(nombre="P4", marcas="MP4", precio=5500, creado="2022-04-17", proveedor=prov_3)
