from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=250)
    district = models.CharField(max_length=255)

    def __str__(self) :
        return self.city

class Court(models.Model):

    CourtType = [
        ("5","5v5"),
        ("7","7v7"),
        ("11","11v11")
    ]


    court_name = models.CharField(max_length=255)
    court_type = models.CharField(max_length=3, choices= CourtType)
    location = models.ForeignKey(Location,on_delete = models.CASCADE )
    availability = models.BooleanField()
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self) :
        return self.court_name
