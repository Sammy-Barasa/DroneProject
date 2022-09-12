from django.urls import path
from FlightSchedule.views import index

urlpatterns = [
       path("",index),
]