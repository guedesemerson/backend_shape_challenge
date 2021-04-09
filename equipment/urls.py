from django.urls import path
from .views import (RegisterNewEquipmentView,
                    ListEquipmentView,
                    RetrieveEquipmentView,
                    InactivateEquipmentView,
                    ActiveEquipmentsFromVesselView)

app_name = "api-equipment"

urlpatterns = [
    path('register_equipment', RegisterNewEquipmentView.as_view(), name='register_equipment'),
    path('list_equipment', ListEquipmentView.as_view(), name='list_equipment'),
    path('retrieve_equipment/<str:equipment_code>', RetrieveEquipmentView.as_view(), name='retrieve_equipment'),
    path('active_equipments_from_vessel/<str:vessel_code>', ActiveEquipmentsFromVesselView.as_view(),
         name='active_equipments_from_vessel'),
    path('inactivate_equipment', InactivateEquipmentView.as_view(), name='inactivate_equipment'),
]