from django.shortcuts import render, HttpResponseRedirect
from models.models import Potholes, WorkOrder, DamageFile, RepairCrew, Equipment
from django.db.models import Q
from random import randint
# Create your views here.

def admin_page_render(request):
    return render(request, "admin_page.html")

def modify(request):
    street_address = request.POST.get('street_address')
    status = request.POST.get('status')
    pothole = Potholes.objects.get(street_address = street_address)
    WorkOrder.objects.filter(pothole_id = pothole.id).update(status = status)
    return HttpResponseRedirect('/')