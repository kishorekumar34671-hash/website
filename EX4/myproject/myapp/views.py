
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "map.html")

def place1(request):
    return render(request,'p1.html')

def place2(request):
    return render(request,'p2.html')
    

def place3(request):
    return render(request,'p3.html' )

def place4(request):
    return render(request,'p4.html')

def place5(request):
    return render(request,'p5.html')
