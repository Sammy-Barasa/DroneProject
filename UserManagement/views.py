from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from UserManagement.serializers import RegisterSerializer
# Create your views here.

from django.contrib.auth import get_user_model

@api_view(['GET'])
def index(request):
    return Response({"Message": "UserAPIEndpoint"})

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.validated_data
        # use saved email to send verifying link
        validated_user = get_user_model().objects.get(email=user_data['email'])