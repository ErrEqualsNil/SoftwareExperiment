from django.shortcuts import render
from models.models import Potholes, WorkOrder
from django.db.models import Q
# Create your views here.


def main_page_render(request):
    potholes = Potholes.objects.all()
    data = [{
        'street_address': pothole.street_address,
        'size': pothole.size,
        'location': pothole.location,
        'district': pothole.district,
        'status': WorkOrder.objects.filter(pothole=pothole)[0].status
    } for pothole in potholes]
    return render(request, "main_page.html", {'potholes': data})
