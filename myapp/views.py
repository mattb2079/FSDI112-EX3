from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is the home screen")

#-------------

def about(request):
    return HttpResponse("<h3>Matt Bishop's about page</h3>")