from rest_framework import serializers
from .models import Location, LocationSet

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['pk', 'latitude', 'longitude','create_date','location_set']

        read_only_fields = ['create_date','location_set']

class LocationSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationSet
        fields = ['pk', 'create_date', 'last_change', 'locations','is_active']

        read_only_fields = ['create_date', 'last_change', 'locations', 'is_active']