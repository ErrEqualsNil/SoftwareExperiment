from django.shortcuts import render
from models.models import Potholes, WorkOrder
from django.db.models import Q
# Create your views here.


def main_page_render(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    print(ip)
    data = WorkOrder.objects.all().filter(~Q(status="finish"))
    data = [i.pothole for i in data]
    return render(request, "main_page.html", {'potholes': data})
