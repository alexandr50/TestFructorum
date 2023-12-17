from rest_framework import generics

from .models import Complation
from .serializers import CreateComplationSerializer, UpdateComplationSerializer, ComplationSerializer


class CreateComplationView(generics.CreateAPIView):
    queryset = Complation.objects.all()
    serializer_class = CreateComplationSerializer


class DeleteComplationView(generics.DestroyAPIView):
    queryset = Complation.objects.all()
    serializer_class = CreateComplationSerializer


class UpdateComplationView(generics.UpdateAPIView):
    queryset = Complation.objects.all()
    serializer_class = UpdateComplationSerializer


class ListComplationView(generics.ListAPIView):
    queryset = Complation.objects.all()
    serializer_class = ComplationSerializer
