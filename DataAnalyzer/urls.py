from django.urls import path
from DataAnalyzer.views import index

urlpatterns =[
    path("",index),
]