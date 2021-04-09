from rest_framework import serializers
from .models import Vessel
from equipment.models import Equipment


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = (
            'vessel_code',
        )


class VesselRetrieveSerializer(serializers.ModelSerializer):
    equipments = serializers.SerializerMethodField()

    class Meta:
        model = Vessel
        fields = (
            'vessel_code',
            'equipments'
        )

    def get_equipments(self, obj):
        equipments = Equipment.objects.filter(vessel=obj)
        equipments = equipments.values()
        return equipments
