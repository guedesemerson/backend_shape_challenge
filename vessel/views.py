from rest_framework.generics import (ListAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView)
from .serializers import VesselSerializer, VesselRetrieveSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vessel


class RegisterNewVesselView(GenericAPIView):
    serializer_class = VesselSerializer

    def post(self, request):
        serializer = VesselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListVesselView(ListAPIView):

    serializer_class = VesselSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vessel_code']

    def get_queryset(self):
        return Vessel.objects.all()


class RetrieveVesselView(RetrieveAPIView):

    serializer_class = VesselRetrieveSerializer
    lookup_field = "vessel_code"

    def get_queryset(self):
        return Vessel.objects.filter(vessel_code=self.kwargs['vessel_code'])