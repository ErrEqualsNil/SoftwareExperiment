from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_page_render),
    path('modify', views.modify)

]