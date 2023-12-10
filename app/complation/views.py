from rest_framework import generics

from .models import Complation
from .serializers import CreateComplationSerializer


class CreateComplationView(generics.CreateAPIView):
    queryset = Complation.objects.all()
    serializer_class = CreateComplationSerializer


class DeleteComplationView(generics.DestroyAPIView):
    queryset = Complation.objects.all()
    serializer_class = CreateComplationSerializer
