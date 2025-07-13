from django.urls import  path
from . import views
urlpatterns = [
    #   path("",views.empty), 
    path("january",views.index) ,
    path("febraury",views.empty)
]

