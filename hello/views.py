from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello</h1>")

def aboutus(request):
    return HttpResponse("<h1 style='color:blue'>About Us</h1>")

def contactus(request):
    return HttpResponse("<h1>Contact Us</h1>")