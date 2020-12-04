from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.submit_page_render),  # 提交报告
    path('finishsubmit', views.process_submit),
]
