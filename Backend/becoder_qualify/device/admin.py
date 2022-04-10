from django.contrib import admin
from .models import DeviceData, SmartDevice
# Register your models here.

admin.site.register(SmartDevice)
admin.site.register(DeviceData)