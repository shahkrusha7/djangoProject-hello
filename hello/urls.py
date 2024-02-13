from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='hello-home'),
    path('aboutus/', aboutus, name='hello-aboutus'),
    path('contactus/', contactus, name='hello-contactus')
]