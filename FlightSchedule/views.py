from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from FlightSchedule.serializers import DroneFlightSerializer, DroneFlightCreateSerializer
from rest_framework.exceptions import ValidationError
from FlightSchedule.models import DroneFlight
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Message": "FlightAPIEndpoint"})


class DroneFlightCreateView(generics.GenericAPIView):
    
    serializer_class = DroneFlightCreateSerializer

    # create work for user
    def post(self, request,user_id):
        data = request.data
        # print(request.user)
        print(request.data)
        serializer = self.serializer_class(data=data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            print(serializer.data)
            return Response(data={"message": "Drone Flight Has Been created"}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            print(error)
            print(serializer.errors)
            return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class DroneFlightCreateView(generics.GenericAPIView):
    
    serializer_class = DroneFlightCreateSerializer

    # create work for user
    def post(self, request,user_id):
        data = request.data
        # print(request.user)
        print(request.data)
        serializer = self.serializer_class(data=data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            print(serializer.data)
            return Response(data={"message": "Drone Flight Has Been created"}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            print(error)
            print(serializer.errors)
            return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class DroneFlightView(generics.GenericAPIView):
   
    serializer_class= DroneFlightSerializer
    
    # overriding get queryset
    def get_queryset(self):
        """
        returns works for the specific user
        """
        queryset = DroneFlight.objects.all()
        if queryset is not None:
            # return queryset.filter(scheduled_date=user).order_by('-last_modified')
            return queryset.order_by('-last_modified')
    
    def get(self,request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)


class DroneFlightIndividualView(generics.GenericAPIView):
    # overriding get queryset
    def get_queryset(self):
        """
        returns works for the specific user
        """
        queryset = DroneFlight.objects.all()
        id = self.kwargs['user_id']
        user = get_user_model().objects.get(pk=id)
        if user is not None:
            return queryset.filter(user_id=user.id).order_by('-last_modified')
    
    def get(self,request,user_id):
        serializer = self.serializer_class(self.get_queryset(), many=True)  
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)