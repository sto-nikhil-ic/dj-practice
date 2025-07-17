from django.urls import  path
from . import views
urlpatterns = [
    path("",views.empty), 
    path("<int:month>",views.number),
    path("<str:month>",views.months,name="month-") 
    
]

