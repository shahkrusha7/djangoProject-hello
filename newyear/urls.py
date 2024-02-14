from django.urls import path
from .views import home,employeeview,productview

urlpatterns = [
path("",home,name="newyear-home"),
    path("employee/",employeeview,name="employeeview"),
    path("product/",productview,name="productview")
]