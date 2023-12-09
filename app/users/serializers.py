from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = CustomUser.objects.create(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
