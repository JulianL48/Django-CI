import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

#Obtenemos el GETALL de las diferentes tablas
@pytest.mark.django_db
@pytest.mark.parametrize('url_name', 
    [
        'sector-list-create',
        'proveedor-list-create',
        'producto-list-create'
    ]
)
def test_get_all(url_name):
    client = APIClient()
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


#Obtenemos los productos mayores que 5000
@pytest.mark.usefixtures("create_products")
@pytest.mark.django_db
def test_get_products_mayor_5000():
    client = APIClient()
    url = reverse('productos_mayor_que_5000')
    response = client.get(url)
    print('Vida HPTA')
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


#Obtenemos los productos por proveedores
@pytest.mark.usefixtures("create_products")
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("data,expected_status,expected_field_errors",
    [(
        {"proveedor_id": "1"}, status.HTTP_200_OK, {}
    )]
)
def test_products_by_proveedor(data, expected_status, expected_field_errors):
    client = APIClient()
    url = reverse('productos_por_proveedor_post')
    response = client.post(url, data, format='json')
    print(response.data)
    assert response.status_code == expected_status