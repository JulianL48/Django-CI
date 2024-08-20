import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


#---------------------------- Sector ----------------------------#
@pytest.mark.django_db()
@pytest.mark.parametrize("data,expected_status",
    [(
        {
            "nombre": "Test_Sector",
            "caracteristica": "Prueba_caracteristica"
        }, status.HTTP_201_CREATED
    )]
)
def test_create_sector(data, expected_status):
    client = APIClient()
    url = reverse('sector-list-create')
    response = client.post(url, data, format='json')
    assert response.status_code == expected_status


#Update de sector
@pytest.mark.usefixtures("create_sectors")
@pytest.mark.django_db()
@pytest.mark.parametrize("sector_id, data, expected_status",
    [
        (2,{"nombre": "Test_Sector","caracteristica": "Prueba_caracteristica"}, status.HTTP_200_OK)
    ],
)
def test_update_sector(sector_id, data, expected_status):
    client = APIClient()
    url = reverse('sector-detail', args=[sector_id])
    response = client.put(url, data, format='json')
    assert response.status_code == expected_status

#Eliminacion de sector
@pytest.mark.usefixtures("create_sectors")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("sector_id, expected_status",
    [
        (2, status.HTTP_204_NO_CONTENT),
        (99, status.HTTP_404_NOT_FOUND)
    ],
)
def test_delete_sector(sector_id, expected_status):
    client = APIClient()
    url = reverse('sector-detail', args=[sector_id])
    response = client.delete(url)
    assert response.status_code == expected_status


#---------------------------- Proveedores ----------------------------#
@pytest.mark.usefixtures("create_sectors")
@pytest.mark.django_db()
@pytest.mark.parametrize("data,expected_status",
    [(
        {
            "nombre": "Test_Sector",
            "nit": 89026582,
            "sector_fk": 1
        }, status.HTTP_201_CREATED
    )]
)
def test_create_prov(data, expected_status):
    client = APIClient()
    url = reverse('proveedor-list-create')
    response = client.post(url, data, format='json')
    assert response.status_code == expected_status


#Update prov
@pytest.mark.usefixtures("create_proveedors")
@pytest.mark.django_db()
@pytest.mark.parametrize("prov_id, data, expected_status",
    [
        (2,{"nombre": "Test_Prov","nit": 1111111, "sector_fk":2 }, status.HTTP_200_OK)
    ],
)
def test_update_prov(prov_id, data, expected_status):
    client = APIClient()
    url = reverse('proveedor-detail', args=[prov_id])
    response = client.put(url, data, format='json')
    assert response.status_code == expected_status

#Eliminacion prov
@pytest.mark.usefixtures("create_proveedors")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("prov_id, expected_status",
    [
        (2, status.HTTP_204_NO_CONTENT),
        (99, status.HTTP_404_NOT_FOUND)
    ],
)
def test_delete_prov(prov_id, expected_status):
    client = APIClient()
    url = reverse('proveedor-detail', args=[prov_id])
    response = client.delete(url)
    assert response.status_code == expected_status


#---------------------------- Productos ----------------------------#
@pytest.mark.usefixtures("create_products")
@pytest.mark.django_db()
@pytest.mark.parametrize("data,expected_status",
    [(
        {
            "nombre": "Test_Product",
            "descripcion": "MarcaTest",
            "precio": 70000,
            "creado": "2024-08-12",
            "proveedor": 1
        }, status.HTTP_201_CREATED
    )]
)
def test_create_prod(data, expected_status):
    client = APIClient()
    url = reverse('producto-list-create')
    response = client.post(url, data, format='json')
    assert response.status_code == expected_status


#Update producto
@pytest.mark.usefixtures("create_products")
@pytest.mark.django_db()
@pytest.mark.parametrize("prod_id, data, expected_status",
    [
        (2,{
            "nombre": "Test_ProductUpd",
            "descripcion": "MarcaTest1",
            "precio": 50000,
            "creado": "2024-08-12",
            "proveedor": 2
        }, status.HTTP_200_OK)
    ],
)
def test_update_prod(prod_id, data, expected_status):
    client = APIClient()
    url = reverse('producto-detail', args=[prod_id])
    response = client.put(url, data, format='json')
    assert response.status_code == expected_status

#Eliminacion producto
@pytest.mark.usefixtures("create_products")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("prod_id, expected_status",
    [
        (2, status.HTTP_204_NO_CONTENT),
        (9, status.HTTP_404_NOT_FOUND)
    ],
)
def test_delete_prod(prod_id, expected_status):
    client = APIClient()
    url = reverse('producto-detail', args=[prod_id])
    response = client.delete(url)
    assert response.status_code == expected_status

#----------------------------   Clientes ----------------------------#
@pytest.mark.django_db()
@pytest.mark.parametrize("data,expected_status",
    [(
        {
            "nombre": "cliente_Name",
            "direccion": "DirCliente",
            "telefono": 3205648177,
            "email": "puebas@hotmail.com"
        }, status.HTTP_201_CREATED
    )]
)
def test_create_cliente(data, expected_status):
    client = APIClient()
    url = reverse('cliente-list-create')
    response = client.post(url, data, format='json')
    assert response.status_code == expected_status


#Update cliente
@pytest.mark.usefixtures("create_clientes")
@pytest.mark.django_db()
@pytest.mark.parametrize("cliente_id, data, expected_status",
    [
        (2,{
            "nombre": "cliente_Name_Update",
            "direccion": "DirCliente_update",
            "telefono": 111111,
            "email": "puebasUpdate@hotmail.com"
        }, status.HTTP_200_OK)
    ],
)
def test_update_cliente(cliente_id, data, expected_status):
    client = APIClient()
    url = reverse('cliente-detail', args=[cliente_id])
    response = client.put(url, data, format='json')
    assert response.status_code == expected_status

#Eliminacion cliente
@pytest.mark.usefixtures("create_clientes")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("clie_id, expected_status",
    [
        (2, status.HTTP_204_NO_CONTENT),
        (9, status.HTTP_404_NOT_FOUND)
    ],
)
def test_delete_cliente(clie_id, expected_status):
    client = APIClient()
    url = reverse('cliente-detail', args=[clie_id])
    response = client.delete(url)
    assert response.status_code == expected_status

#----------------------------   Facturas ----------------------------#
@pytest.mark.usefixtures("create_factura")
@pytest.mark.django_db()
@pytest.mark.parametrize("data,expected_status",
    [(
        {
           "cliente_id": 1,
            "fecha_emision": "2024-08-16",
            "fecha_vencimiento": "2024-09-16",  # Suponiendo vencimiento en 30 días
            "total": 0
        }, status.HTTP_201_CREATED
    )]
)
def test_create_factura(data, expected_status):
    client = APIClient()
    url = reverse('factura-list-create')
    response = client.post(url, data, format='json')
    assert response.status_code == expected_status


#Update factura
@pytest.mark.usefixtures("create_factura")
@pytest.mark.django_db()
@pytest.mark.parametrize("factura_id, data, expected_status",
    [
        (2,{
            "cliente_id": 1,
            "fecha_emision": "2024-08-16",
            "fecha_vencimiento": "2024-09-16",  # Suponiendo vencimiento en 30 días
            "total": 1000.00
        }, status.HTTP_200_OK)
    ],
)
def test_update_factura(factura_id, data, expected_status):
    client = APIClient()
    url = reverse('factura-detail', args=[factura_id])
    response = client.put(url, data, format='json')
    assert response.status_code == expected_status

#Eliminacion factura
@pytest.mark.usefixtures("create_factura")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("factura_id, expected_status",
    [
        (2, status.HTTP_204_NO_CONTENT),
        (9, status.HTTP_404_NOT_FOUND)
    ],
)
def test_delete_factura(factura_id, expected_status):
    client = APIClient()
    url = reverse('factura-detail', args=[factura_id])
    response = client.delete(url)
    assert response.status_code == expected_status