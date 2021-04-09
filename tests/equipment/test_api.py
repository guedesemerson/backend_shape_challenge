import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


def test_equipment_api_create(admin_client, vessel):
    equipment_object = {
        'equipment_code': '5310B9D7',
        'name': 'teste_equipment_name',
        'status': True,
        'location': 'test_location_name',
        'vessel_code': vessel.vessel_code
    }
    url = reverse('api-equipment:register_equipment')
    response = admin_client.post(url, data=equipment_object)
    assert response.status_code == status.HTTP_201_CREATED


def test_equipment_list(admin_client):
    url = reverse('api-equipment:list_equipment')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_equipment_api_detail(admin_client, equipment):
    url = reverse('api-equipment:retrieve_equipment', args=[equipment.equipment_code])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['equipment_code'] == equipment.equipment_code


def test_active_equipments_from_vessel_api_detail(admin_client, vessel):
    url = reverse('api-equipment:active_equipments_from_vessel', args=[vessel.vessel_code])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_inactivate_equipment_api_create(admin_client, equipment):
    equipments_code = {
        'equipments_code': [equipment.equipment_code]
    }
    url = reverse('api-equipment:inactivate_equipment')
    response = admin_client.post(url, data=equipments_code)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
