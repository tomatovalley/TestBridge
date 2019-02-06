<<<<<<< HEAD
from rest_framework import serializers
from Devices.models import Device


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id","device","category","os","version","creationDate","updatedDate")
        
    def get_url(self, obj):
        request = self.context.get("request")
=======
from rest_framework import serializers
from Devices.models import Device


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id","device","category","os","version","creationDate","updatedDate")
        
    def get_url(self, obj):
        request = self.context.get("request")
>>>>>>> 1e76af9444df3aa6779f6bd26b224af9d9dea43c
        return obj.get_api_url(request=request)