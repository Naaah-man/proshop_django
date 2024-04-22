from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
      # to customize the response 
      data = super().validate(attrs)
      
      serializer = UserSerializerWithToken(self.user).data
      
      for k, v in serializer.items():
        data[k] = v
      
      return data
      
class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer
  
@api_view(['POST'])
def registerUser(request):
  try:
    data = request.data
    user = User.objects.create(
      first_name = data['name'],
      username = data['email'],
      email = data['email'],
      password = make_password(data['password'])
    )
    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)
  except:
    message = {'detail': "User with this email already exist"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getUserProfile(request):
  
  # unlike as its default behaviour to grab user credentials it will now fetch token credentials
  user = request.user
  
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
  users = User.objects.all()
  
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)
