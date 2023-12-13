from rest_framework import serializers
from .models import Complation


class CreateComplationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complation
        fields = ('title', 'short_description')


class UpdateComplationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complation
        fields = ('title', 'short_description')
