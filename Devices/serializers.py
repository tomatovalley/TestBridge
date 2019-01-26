from rest_framework import serializers
from Devices.models import Device


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id","device","category","os","version","creationDate","updatedDate")