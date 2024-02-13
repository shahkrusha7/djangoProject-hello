from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"hello/home.html")

def aboutus(request):
    return render(request,"hello/aboutus.html")

def contactus(request):
    return render(request,"hello/contactus.html")