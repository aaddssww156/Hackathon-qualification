from email.policy import default
from django.db import models

# Create your models here.
class SmartDevice(models.Model):
    """
    model for categories smart devices
    """
    name = models.CharField(max_length=120)
    
    def __str__(self)->str:
        return self.name
    
class DeviceData(models.Model):
    """
    data from smart_devices
    """
    timedd = models.DateTimeField()#auto_now_add=True, editable=True)
    data = models.FloatField()
    smartdevice_id = models.ForeignKey(SmartDevice, on_delete=models.CASCADE)
