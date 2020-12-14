from django.shortcuts import render, HttpResponseRedirect
from models.models import Potholes, WorkOrder
from django.db.models import Q
from random import randint


# Create your views here.


def get_repair_crew_numbers(work_order):
    repair_crews = work_order.repair_crew
    if repair_crews == None:
        return 0
    return repair_crews.num_of_people


def admin_page_render(request):
    work_orders = WorkOrder.objects.all()
    data = []
    for work_order in work_orders:
        num_people = get_repair_crew_numbers(work_order)
        data.append({
            "work_order": work_order,
            "num_people": num_people,
        })
    return render(request, "admin_page.html", {"work_orders": data})


def modify(request):
    work_order_id = request.GET.get('id')
    status = request.GET.get('status')
    work_order = WorkOrder.objects.filter(id=work_order_id)[0]
    work_order.status = status
    work_order.save()
    return HttpResponseRedirect('/admini')
