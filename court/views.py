from django.shortcuts import render
from .models import Court
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,generics,filters
from django.contrib.auth.models import User
from .serializer import CourtSerializer,DeleteSerializer,SearchSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def list_Court (request): 
        
        queryset = Court.objects.all()
        serializers = CourtSerializer(queryset, many = True)
        return Response(serializers.data)


@api_view(['PUT','GET'])
def Update_court(request,pk):
        
         
        if request.method == 'PUT':
                court = Court.objects.get(pk=pk)
                serailizer = CourtSerializer(court,data = request.data)
                if serailizer.is_valid():
                        serailizer.save()
                        return Response(serailizer.data,status=status.HTTP_201_CREATED)
                return Response(serailizer.data, status = status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
                queryset = Court.objects.get(pk=pk)
                serailizer = CourtSerializer(queryset)

                return Response(serailizer.data)
                

@api_view(['DELETE'])
def delete_court(request,pk): 
        queryset = Court.objects.get(pk=pk)
        print(queryset),

        queryset.delete()
        return Response({'msg': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



@api_view([ 'POST'])
def Search_Court(request):
    if request.method == 'POST':
        court_name = request.data.get('court_name')         
        courts = Court.objects.filter(court_name__icontains=court_name)
        serializer = SearchSerializer(courts , many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
print(Court.objects.filter(court_name = 'Camnou'))
