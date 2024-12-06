from rest_framework import serializers
from .models import Court, Location

# Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # No need to set 'model' manually; it's inferred automatically
        fields = '__all__'

# Court Serializer
class CourtSerializer(serializers.ModelSerializer): 
    location = LocationSerializer()  
    class Meta:
        model = Court
        fields = '__all__'

# Delete Serializer
class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['id']
