from django.http import HttpResponse
from django.shortcuts import render

# Function returning HttpResponse
def hello(request):
    return HttpResponse("<h1>Hello, this is HttpResponse!</h1>")

# Function rendering HTML template
def home(request):
    return render(request, 'home.html')
