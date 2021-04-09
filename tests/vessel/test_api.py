import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


def test_register_new_vessel(admin_client):
    user_object = {
        "vessel_code": 'MV102'
    }
    url = reverse('api-vessel:register_vessel')
    response = admin_client.post(url, data=user_object)

    assert response.status_code == status.HTTP_201_CREATED


def test_vessel_api_list(admin_client):
    url = reverse('api-vessel:list_vessel')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_vessel_api_detail(admin_client, vessel):
    url = reverse('api-vessel:retrieve_vessel', args=[vessel.vessel_code])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['vessel_code'] == vessel.vessel_code


