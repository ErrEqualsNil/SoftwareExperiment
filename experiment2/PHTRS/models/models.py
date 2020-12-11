from django.db import models

# Create your models here.


class Potholes(models.Model):
    street_address = models.CharField(max_length=80)
    size = models.IntegerField()
    location = models.CharField(max_length=20)  # 2 status: middle, curb
    district = models.CharField(max_length=50)
    repair_priority = models.IntegerField(blank=True, null=True)


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50)
    equipment_price = models.IntegerField(default=10)


class RepairCrew(models.Model):
    num_of_people = models.IntegerField()
    isBusy = models.BooleanField(default=False)
    leader = models.CharField(max_length=20)
    equipments = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING, blank=True, null=True)


class WorkOrder(models.Model):
    pothole = models.OneToOneField(Potholes, on_delete=models.CASCADE)
    repair_crew = models.OneToOneField(RepairCrew, on_delete=models.DO_NOTHING, blank=True, null=True)
    hours_applied = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)  # 3 status: waiting; repairing; finish
    filter_material = models.CharField(default="Nothing", max_length=50, blank=True, null=True)
    cost = models.IntegerField(default=10, blank=True, null=True)


class ReportFile(models.Model):
    pothole = models.OneToOneField(Potholes, on_delete=models.CASCADE)
    citizen_name = models.CharField(max_length=50)
    citizen_address = models.CharField(max_length=100)
    citizen_phone_number = models.CharField(max_length=20)

