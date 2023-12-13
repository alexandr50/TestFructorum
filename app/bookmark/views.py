from rest_framework import generics

from complation.models import Complation
from .models import Bookmark
from .serializers import CreateBookmarkSerializer, AddBookToComplation


class CreateBookmarkView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer


class DeleteBookmarkView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer


class AddBookmarkToComplationView(generics.UpdateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = AddBookToComplation

    def update(self, request, *args, **kwargs):
        complation_id = kwargs['pk']
        try:
            complation = Complation.objects.get(id=complation_id)
        except Exception:
            raise 'Not Found'
        self.complation = complation
        self.save()