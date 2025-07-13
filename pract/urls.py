from django.urls import  path
from . import views
urlpatterns = [
    #   path("",views.empty), 
    path("<month>",views.index) ,
   
]

