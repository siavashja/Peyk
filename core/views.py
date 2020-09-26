from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from rest_framework.views import APIView
from .models import Location, LocationSet
from .serializers import LocationSerializer, LocationSetSerializer
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

class LocationSetCreateView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = LocationSet.objects.all()
    serializer_class = LocationSetSerializer

    def perform_create(self,serializer):
        location_set = serializer.save(user_profile=self.request.user.user_profile)
        location_set.save()
        return HttpResponse(status=204)


class LocationCreateView(CreateAPIView):
    
    permission_classes= (IsAuthenticated,)
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def perform_create(self,serializer):
        user_profile = self.request.user.user_profile
        location_set = user_profile.location_sets.last()

        if location_set.is_active:
            location = serializer.save(location_set= location_set)
            location.save()
        return HttpResponse(status=204)

class LocationSetEndView(APIView):

    permission_classes= (IsAuthenticated,)
    #serializer_class = LocationSetSerializer
    queryset = LocationSet.objects.all()

    def post(self, request, *args, **kwargs):
        user_profile = self.request.user.user_profile
        location_set = user_profile.location_sets.last()
        location_set.is_active = False
        location_set.save()

        return HttpResponse(status=204)

