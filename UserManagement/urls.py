from django.urls import path
from UserManagement.views import index

urlpatterns = [
    path('', index),
   
]