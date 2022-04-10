from datetime import datetime, timedelta

def filter_by_device_and_time(queryset, id_smartdevice:int=None, timestamp:str=None):
    if id_smartdevice is not None:
            queryset = queryset.filter(smartdevice_id=id_smartdevice)
    if timestamp is not None:
            hours_ago = datetime.today() - timedelta(hours=int(timestamp))
            queryset = queryset.filter(timedd__gt=hours_ago)
    return queryset