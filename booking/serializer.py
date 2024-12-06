from rest_framework import serializers 
from .models import Booking
from  django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id','username']

class BookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Booking
        fields = '__all__'



class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Booking
        fields = ['total_cost']

    # def update(self,instance, validated_data): 

    #     instance.total_cost = validated_data.get('total_cost', instance.total_cost)

    #     instance.save()
    #     return instance 