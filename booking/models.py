from django.db import models
from django.contrib.auth.models import User

from court.models import Court
# Create your models here.


class Booking(models.Model):

    StatusType = [
        ('C','Confirm'),
        ('P','Pending'),
        ('Ca','Cancel')
    ]
    PaymentStatus = [
        ('U','Unpaid'),
        ('P','Paid')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    court = models.ForeignKey(Court, on_delete= models.CASCADE)
    booking_date = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=3, choices = StatusType)
    payment_status = models.CharField(max_length=2, choices = PaymentStatus)
    Created_at = models.DateTimeField()
    update_at = models.DateTimeField