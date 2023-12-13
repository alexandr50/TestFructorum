from rest_framework import generics

from .models import Bookmark
from .serializers import CreateBookmarkSerializer


class CreateBookmarkView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer


class DeleteBookmarkView(generics.DestroyAPIView):
    pass