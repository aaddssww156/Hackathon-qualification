from rest_framework import serializers
from .models import DeviceData, SmartDevice

class SmartDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartDevice
        fields = ['id', 'name']

class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ['id', 'timedd', 'data', 'smartdevice_id']
        
class DeviceDataGetSerializer(serializers.ModelSerializer):
    timedd = serializers.DateTimeField(format="%H:%M:%S")
    class Meta:
        model = DeviceData
        fields = ['timedd', 'data']