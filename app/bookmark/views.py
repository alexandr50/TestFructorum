from rest_framework import generics
from rest_framework.response import Response

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
        bookmark = Bookmark.objects.get(pk=kwargs['pk'])
        for com_id in request.data['complation']:
            complation = Complation.objects.filter(id=com_id)
            if complation:
                bookmark.complation.set(complation)
                bookmark.save()

        return Response('Done')

    def get_queryset(self):
        pass

    def perform_update(self, serializer):
        pass