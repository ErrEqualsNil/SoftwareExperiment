from django.db import models

# Create your models here.


class Potholes(models.Model):
    street_address = models.CharField(max_length=80)
    size = models.IntegerField()
    location = models.CharField(max_length=20)  # 2 status: middle, curb
    district = models.CharField(max_length=50)
    repair_priority = models.IntegerField()


class RepairCrew(models.Model):
    num_of_people = models.IntegerField()


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50)
    equipment_number = models.IntegerField(default=0)
    equipment_price = models.IntegerField(default=10)


class WorkOrder(models.Model):
    pothole = models.OneToOneField(Potholes, on_delete=models.CASCADE)
    repair_crew = models.ForeignKey(RepairCrew, on_delete=models.DO_NOTHING)
    equipment_assigned = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING)
    hours_applied = models.IntegerField()
    status = models.CharField(max_length=20)  # 3 status: waiting; repairing; finish
    filter_material = models.CharField(default="Nothing", max_length=50)
    cost = models.IntegerField(default=10)


class DamageFile(models.Model):
    pothole = models.OneToOneField(Potholes, on_delete=models.CASCADE)
    citizen_name = models.CharField(max_length=50)
    citizen_address = models.CharField(max_length=100)
    citizen_phone_number = models.CharField(max_length=20)

