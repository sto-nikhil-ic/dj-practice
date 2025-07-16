from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create you views here.
month_data = {
    "january": "this is january",
    "february": "this is february",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "october": "this is october",
    "november": "this is november",
    "december": "this is december"
}

def number(request,month):
    return HttpResponse(month)


def months(request, month):
    try:
        text=month_data[month]
    except:
            return HttpResponse("errror month")
    
    return HttpResponse(text)
    
    