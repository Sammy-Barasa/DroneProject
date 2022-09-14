from django.db import models
from UserManagement.models import DroneUAV, User

class DroneFlight(models.Model):
    user_id = models.ForeignKey(to=User)
    drone_id = models.ForeignKey(to=DroneUAV)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField()
    scheduled_time_from = models.TimeField()
    scheduled_time_to = models.TimeField()
    flight_approved = models.BooleanField()
    approved_at = models.DateTimeField(auto_now=True)
    # flight_data = models.JSONField() # analyzed flight data
    
