from rest_framework import serializers
from equipment.models import Equipment
from vessel.models import Vessel


class EquipmentSerializer(serializers.ModelSerializer):
    vessel_code = serializers.CharField(write_only=True)
    vessel = serializers.HiddenField(default=1)

    class Meta:
        model = Equipment
        fields = (
            'id',
            'name',
            'equipment_code',
            'location',
            'vessel_code',
            'vessel',

        )
        read_only_fields = [
            'id',
        ]

    def create(self, validated_data):
        vessel_code = validated_data['vessel_code']
        if not Vessel.objects.filter(vessel_code=vessel_code).exists():
            raise serializers.ValidationError(
                {'vessel': 'Vessel code does not exists'})
        else:
            vessel_object = Vessel.objects.get(vessel_code=vessel_code)
            del validated_data['vessel_code']
        validated_data['vessel'] = vessel_object

        return Equipment.objects.create(**validated_data)


class EquipmentListRetrieveSerializer(serializers.ModelSerializer):
    vessel = serializers.CharField(source='vessel.vessel_code', required=False)
    status = serializers.SerializerMethodField(method_name='set_status')

    class Meta:
        model = Equipment
        fields = (
            'name',
            'equipment_code',
            'location',
            'status',
            'vessel',
        )

    def set_status(self, instance):
        if instance.status == True:
            return "active"
        else:
            return "inactive"


class InactivateEquipmentSerializer(serializers.ModelSerializer):
    equipments_code = serializers.ListField(write_only=True)

    class Meta:
        model = Equipment
        fields = (
            'equipments_code',
        )