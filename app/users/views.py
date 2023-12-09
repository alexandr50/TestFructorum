from rest_framework import generics

from .models import CustomUser
from .serializers import UserRegisterSerializer, UserSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class UsersListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



