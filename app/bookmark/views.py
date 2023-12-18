from rest_framework import generics
from rest_framework.response import Response

from complation.models import Complation
from .models import Bookmark
from .serializers import CreateBookmarkSerializer, AddBookToComplation, UrlSerializer
from .services import get_content


class CreateBookmarkView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        url = request.data['url']
        if url:
            content = get_content(url)
            Bookmark.objects.create(**content)
        return Response('Заметка создана')


class DeleteBookmarkView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer


class AddBookmarkToComplationView(generics.UpdateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = AddBookToComplation

    def update(self, request, *args, **kwargs):
        bookmark = Bookmark.objects.get(pk=kwargs['pk'])
        for com_id in request.data['complation']:
            complation = Complation.objects.filter(id=com_id['id'])
            if complation:
                bookmark.complation.set(complation)
                bookmark.save()

        return Response('Вы добавили заметку в коллекцию')

