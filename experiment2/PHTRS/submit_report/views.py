from django.shortcuts import render, HttpResponseRedirect
from models.models import Potholes, WorkOrder, ReportFile, RepairCrew, Equipment
from random import randint
# Create your views here.


def submit_page_render(request):
    return render(request, "submit_page.html")


def calculate_repair_priority(pothole):
    holes_at_this_street = len(Potholes.objects.filter(street_address=pothole.street_address))
    size = pothole.size
    location_weight = 5 if pothole.location == "middle" else 2
    return holes_at_this_street + location_weight + size


def allocate_repair_crew():
    repair_crews = RepairCrew.objects.filter(isBusy=False).order_by('-num_of_people')
    if len(repair_crews) != 0:
        return repair_crews[randint(0, len(repair_crews) - 1)]
    else:
        return -1


def calculate_hours(pothole, repair_crew):
    location_weight = 5 if pothole.location == "middle" else 2
    return (pothole.size + location_weight) / repair_crew.num_of_people


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
                                      district=district)
    pothole.repair_priority = calculate_repair_priority(pothole)
    pothole.save(update_fields=['repair_priority'])

    selected_repair_crew = allocate_repair_crew()
    if selected_repair_crew != -1:
        selected_repair_crew.isBusy = True
        WorkOrder.objects.create(pothole=pothole, repair_crew=selected_repair_crew,
                                 hours_applied=1, status="waiting")
    else:
        WorkOrder.objects.create(pothole=pothole, status="waiting")
    ReportFile.objects.create(pothole=pothole, citizen_name=citizen_name, citizen_address=citizen_address,
                              citizen_phone_number=citizen_phone_number)
    return HttpResponseRedirect('/')
