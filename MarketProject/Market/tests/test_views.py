import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize(
    "data,expected_status,expected_field_errors",
    [
        # Caso 1: JSON completo y válido
        ({
            "nombre": "Test",
            "caracteristica": "Otro"
        }, status.HTTP_201_CREATED, {})
    ]
)
def test_my_view(data, expected_status, expected_field_errors):
    client = APIClient()
    url = reverse('sector-list-create')
    response = client.post(url, data, format='json')

    print("Request data:", data)
    print("Response status code:", response.status_code)
    print("Response data:", response.data)
     # Verificar el código de estado
    assert response.status_code == expected_status

    # Verificar errores de campo si se esperan
    if expected_field_errors:
        for field, expected_error_list in expected_field_errors.items():
            assert field in response.data
            # Convertir ErrorDetail a lista de cadenas para comparación
            actual_errors = [str(e) for e in response.data[field]]
            assert sorted(actual_errors) == sorted(expected_error_list)
    else:
        # Verificar que no haya errores si no se esperan
        assert 'errors' not in response.data

#Obtenemos el GETALL de las diferentes tablas
@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    'sector-list-create',
    'proveedor-list-create',
    'producto-list-create'
])
def test_example_view_get(url_name):
    client = APIClient()
    url = reverse(url_name)
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK