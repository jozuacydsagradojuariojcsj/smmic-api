from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SinkNode)
admin.site.register(SensorNode)
admin.site.register(SMSensorReadings)
admin.site.register(SKReadings)
admin.site.register(SMSensorAlerts)