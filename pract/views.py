from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create you views here.
def index(request, month):
    text=None
    if month == 'january':
        text=  "this is january"
    elif month == 'february':
        text="this is february"
    else:
         return HttpResponseNotFound("not found")
    return HttpResponse(text)
    
    