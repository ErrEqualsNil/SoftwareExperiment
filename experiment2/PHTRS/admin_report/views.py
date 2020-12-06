from django.shortcuts import render, HttpResponseRedirect
from models.models import Potholes, WorkOrder, DamageFile, RepairCrew, Equipment
from django.db.models import Q
from random import randint
# Create your views here.


def admin_page_render(request):
    workorders = WorkOrder.objects.all()
    return render(request, "admin_page.html", {"workorders": workorders})

def modify(request):
    work_order_id = request.GET.get('id')
    status = request.GET.get('status')
    work_order = WorkOrder.objects.filter(id=work_order_id)
    work_order.update(status=status)
    return HttpResponseRedirect('/admini')
