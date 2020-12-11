from django.contrib import admin
from .models import Equipment, RepairCrew, WorkOrder, ReportFile, Potholes
# Register your models here.

admin.site.register(Equipment)
admin.site.register(RepairCrew)
admin.site.register(WorkOrder)
admin.site.register(ReportFile)
admin.site.register(Potholes)
