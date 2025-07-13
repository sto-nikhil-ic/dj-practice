from django.shortcuts import render
from django.http import HttpResponse

# Create you views here.
def index(request):
    return HttpResponse("kam garcha ")
def empty(request):
    return HttpResponse("this is february")