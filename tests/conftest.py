from rest_framework.test import APIClient
from equipment.models import Equipment
from vessel.models import Vessel
import pytest


@pytest.fixture
def admin_client(admin_user):
    client = APIClient()
    return client


@pytest.fixture
def vessel():
    vessel = Vessel()
    vessel.vessel_code = 'MV102'
    vessel.save()
    return vessel


@pytest.fixture
def equipment():
    vessel = Vessel()
    vessel.vessel_code = 'MV102'
    vessel.save()

    equipment = Equipment()
    equipment.equipment_code = '5310B9D7'
    equipment.name = 'equipment_test_name'
    equipment.status = True
    equipment.location = 'test_name_location'
    equipment.vessel = vessel
    equipment.save()
    return equipment