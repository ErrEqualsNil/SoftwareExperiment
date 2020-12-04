from django.shortcuts import render, HttpResponseRedirect
from models.models import Potholes, WorkOrder, DamageFile, RepairCrew, Equipment
from random import randint
# Create your views here.


def submit_page_render(request):
    return render(request, "submit_page.html")


def process_submit(request):
    street_address = request.GET.get('street_address')
    size = request.GET.get('size')
    size = int(size)
    location = request.GET.get('location')
    district = request.GET.get('district')
    citizen_name = request.GET.get('citizen_name')
    citizen_address = request.GET.get('citizen_address')
    citizen_phone_number = request.GET.get('citizen_phone_number')
    pothole = Potholes.objects.create(street_address=street_address, size=size, location=location,
                                      district=district, repair_priority=size)
    repaircrews = RepairCrew.objects.all()
    equipments = Equipment.objects.all()
    workOrder = WorkOrder.objects.create(pothole=pothole, repair_crew=repaircrews[randint(0, len(repaircrews) - 1)],
                                         equipment_assigned=equipments[randint(0, len(equipments) - 1)],
                                         hours_applied=11 - pothole.repair_priority, status="waiting")
    damage_file = DamageFile.objects.create(pothole=pothole, citizen_name=citizen_name, citizen_address=citizen_address,
                                            citizen_phone_number=citizen_phone_number)
    return HttpResponseRedirect('/')
