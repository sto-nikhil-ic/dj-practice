from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    
    if month>12:
        return HttpResponse("errror month")
    
    month=month-1 #LSIT 0 DEKHI SURU HUNCHA
    dicmonth=list(month_data.keys())
    forward_month=dicmonth[month]
    redirect_path =reverse("month-",args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def months(request, month):
    try:
        text=month_data[month]
        html=f"<h1>{text}</h1>"
    except:
            return HttpResponse("errror month")
    
    return HttpResponse(html)
    
    