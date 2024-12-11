from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView ):
    permission_classes = [permissions.AllowAny]

class TokenRefreshView(TokenRefreshView):
    permission_classes= [permissions.AllowAny]


class ProtectedView(APIView): 
    permission_classes=[IsAuthenticated]

    def get(self, request):
        return Response({'message': 'You have authenticated '})