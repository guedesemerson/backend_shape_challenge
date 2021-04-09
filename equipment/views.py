from rest_framework.generics import (ListAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,)
from .serializers import (EquipmentSerializer,
                          EquipmentListRetrieveSerializer,
                          InactivateEquipmentSerializer,)
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Equipment
from vessel.models import Vessel
from rest_framework import serializers


class RegisterNewEquipmentView(GenericAPIView):
    serializer_class = EquipmentSerializer

    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEquipmentView(ListAPIView):

    serializer_class = EquipmentListRetrieveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['equipment_code', ]

    def get_queryset(self):
        return Equipment.objects.all()


class RetrieveEquipmentView(RetrieveAPIView):

    serializer_class = EquipmentListRetrieveSerializer
    lookup_field = "equipment_code"

    def get_queryset(self):
        return Equipment.objects.filter(equipment_code=self.kwargs['equipment_code'])


class ActiveEquipmentsFromVesselView(RetrieveAPIView):

    serializer_class = EquipmentListRetrieveSerializer
    lookup_field = "vessel_code"

    def retrieve(self, request, *args, **kwargs):
        vessel_code = kwargs['vessel_code']
        if not Vessel.objects.filter(vessel_code=vessel_code).exists():
            raise serializers.ValidationError(
                {'equipment': f'vessel:{vessel_code} does not exists'})

        vessel_object = Vessel.objects.get(vessel_code=vessel_code)
        object_result = Equipment.objects.filter(vessel=vessel_object.id, status=True)
        values = object_result.values()
        return Response(values, status.HTTP_200_OK)


class InactivateEquipmentView(GenericAPIView):
    serializer_class = InactivateEquipmentSerializer

    def post(self, request):
        list_equipments = []
        equipments_object = request.data['equipments_code']
        for row in equipments_object:
            if not Equipment.objects.filter(equipment_code=row).exists():
                raise serializers.ValidationError(
                    {'equipment': f'equipment:{row} does not exists'})
            else:
                Equipment.objects.filter(equipment_code=row).update(status=False)
                equipment = Equipment.objects.get(equipment_code=row)
                equipment_object = {
                    "equipment_code": equipment.equipment_code,
                    "name": equipment.name,
                    "vessel_code": equipment.vessel.vessel_code,
                    "status": "Inactive"
                }
                list_equipments.append(equipment_object)

        return Response(list_equipments, status.HTTP_200_OK)
