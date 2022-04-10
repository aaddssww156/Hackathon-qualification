from rest_framework.response import Response
from rest_framework import mixins, viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import DeviceData, SmartDevice
from .serializers import DeviceDataSerializer, DeviceDataGetSerializer, SmartDeviceSerializer
from .services import filter_by_device_and_time


class DeviceDataViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                                                 mixins.CreateModelMixin):
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DeviceDataGetSerializer
        if self.action == 'create':
            return DeviceDataSerializer
    
    queryset = DeviceData.objects.all()
    id_smartdevice = openapi.Parameter('id_smartdevice', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False, description="id of smartdevice")
    timestamp = openapi.Parameter('timestamp', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False, description="hours")
    
    @swagger_auto_schema(manual_parameters=[id_smartdevice, timestamp])
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        
        id_smartdevice = self.request.query_params.get('id_smartdevice', None)
        timestamp = self.request.query_params.get('timestamp', None)
        queryset = filter_by_device_and_time(queryset, id_smartdevice, timestamp)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class SmartDeviceViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = SmartDevice.objects.all()
    serializer_class = SmartDeviceSerializer