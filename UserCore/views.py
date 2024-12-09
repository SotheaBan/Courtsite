from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions

# Create your views here.
@api_view(['POST'])
def RegisterUser(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
