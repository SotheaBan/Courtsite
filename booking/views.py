from django.shortcuts import render
from .serializer import BookingSerializer,UpdateBookingSerializer,UserSerializer
from .models import Booking
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def create_booking(request): 
    serializer = BookingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED) 
    else: 
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def Listing_booking(request):
    queyset = Booking.objects.all()
    serializer = BookingSerializer(queyset,many=True)
     
    return Response(serializer.data)


@api_view(['POST','GET'])
def Update_booking(request,pk):
    if request.method == 'GET' :
        queryset = Booking.objects.filter(pk=pk)
        serializer = BookingSerializer(queryset,many=True)

        return Response(serializer.data)
    if request.method == 'POST':
        booking = Booking.objects.get(pk=pk)
        serializer = UpdateBookingSerializer(booking,data = request.data)

        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)

# Action Controller, View
@api_view(['GET'])
def get_booking_detail(request, pk):
    # get data through model from database
    queryset = Booking.objects.filter(pk=pk)

    # Apply business logic

    # serialize data to convert it to what we want
    serializer = BookingSerializer(queryset, many=True)

    # Response back to endpoint
    return Response(serializer.data)


@api_view(['GET'])
def list_user_booking(reqest):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset , many= True)
    return Response(serializer.data)
 
    

def BookList(request):
    
    if request.user.is_authenticated : 
        booking = Booking.objects.filter(user=request.user)
    else:
        booking= ['Booking none']
    return render(request, 'bookinglist.html', {'booking': booking })  