from rest_framework import serializers
from complation.serializers import ComplationSerializer

from .models import Bookmark


class CreateBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('title', 'short_description', 'link', 'type_link', 'preview')


class AddBookToComplation(serializers.ModelSerializer):
    complation = ComplationSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ('complation',)


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()
