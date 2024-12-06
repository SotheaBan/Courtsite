from django.shortcuts import render
from .models import Court
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import CourtSerializer,DeleteSerializer
# Create your views here.


@api_view(['GET'])
def list_Court (request): 

        queryset = Court.objects.all()
        serializers = CourtSerializer(queryset, many = True)
        return Response(serializers.data)


@api_view(['POST'])
def Update_court(request): 
        
        serailizer = CourtSerializer(data = request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_201_CREATED)
        return Response(serailizer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_court(request,pk): 
        queryset = Court.objects.get(pk=pk)
        print(queryset),

        queryset.delete()
        return Response({'msg': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

