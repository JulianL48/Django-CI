import pytest
from Market.models import Producto, Proveedor, Sector

@pytest.fixture
def create_sectors(db):
    # Creación de sectores
    sectorP = Sector.objects.create(nombre="Primario", caracteristica="SP")
    sectorS = Sector.objects.create(nombre="Secundario", caracteristica="SS")
    sectorT = Sector.objects.create(nombre="Terciario", caracteristica="ST")
    return [sectorP, sectorS, sectorT]

@pytest.fixture
def create_proveedors(create_sectors):
    sectorP, sectorS, sectorT = create_sectors
    # Creación de proveedores
    proveedor1 = Proveedor.objects.create(nombre="Proveedor 1", nit="1818182", sector_fk=sectorP)
    proveedor2 = Proveedor.objects.create(nombre="Proveedor 2", nit="1818182", sector_fk=sectorS)
    proveedor3 = Proveedor.objects.create(nombre="Proveedor 3", nit="1818182", sector_fk=sectorT)
    return [proveedor1, proveedor2, proveedor3]

@pytest.fixture
def create_products(create_proveedors):
    proveedor1, proveedor2, proveedor3 = create_proveedors
    # Crear productos necesarios para la prueba
    Producto.objects.create(nombre="P1", marcas="MP1", precio=6000, creado="2022-02-19", proveedor=proveedor1)
    Producto.objects.create(nombre="P2", marcas="MP2", precio=2000, creado="2022-03-15", proveedor=proveedor2)
    Producto.objects.create(nombre="P3", marcas="MP3", precio=10000, creado="2022-01-20", proveedor=proveedor2)
    Producto.objects.create(nombre="P4", marcas="MP4", precio=5500, creado="2022-04-17", proveedor=proveedor3)
