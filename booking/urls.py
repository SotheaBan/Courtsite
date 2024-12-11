from django.contrib import admin
from django.urls import path
from .views import create_booking,Listing_booking,Update_booking,get_booking_detail,list_user_booking, BookList


app_name = 'booking'
urlpatterns = [
    path('bookinglist/',Listing_booking, ),

    path('create/', create_booking),
    path('update/<int:pk>/', Update_booking),
    path('booking/<int:pk>/', get_booking_detail),
    path('listuser/',list_user_booking),


    path('booking_list/',BookList, name='booking_list')

]
