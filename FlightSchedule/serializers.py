# create a flight

# flight data


from rest_framework import serializers
from FlightSchedule.models import DroneFlight
from django.contrib.auth import get_user_model

class DroneFlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DroneFlight
        fields = ['id','user_id', 'drone_id', 'created_at','scheduled_date','scheduled_time_from', 'flight_approved',
                  'date', 'approved_at']
        read_only_fields = ['id','user_id','drone_id']
        # depth = 1
        # validate
        def validate(self, attr):
            return attr



class DroneFlightCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DroneFlight
        fields = ['user_id', 'drone_id',  'scheduled_date', 'scheduled_time_from']
        
        # validate

        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            user_id = validated_data.pop('user')
            drone_id = validated_data.pop('drone_id')
            scheduled_date = validated_data.pop('scheduled_time_from')
            droneflight = DroneFlight.objects.create(
                
                user_id=user_id, drone_id=drone_id, scheduled_date=scheduled_date,**validated_data)
            return droneflight