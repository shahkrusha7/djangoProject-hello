from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Hello</h1>")
    return render(request,"hello/home.html")

def aboutus(request):
    #return HttpResponse("<h1 style='color:blue'>About Us</h1>")
    return render(request,"hello/aboutus.html")

def contactus(request):
    #return HttpResponse("<h1>Contact Us</h1>")
    return render(request,"hello/contactus.html")