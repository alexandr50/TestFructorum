from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig

from .views import UserRegisterView, UsersListView, ResetTokenAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='create_view'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", UsersListView.as_view(), name="list_view"),
    path("logout/", ResetTokenAPIView.as_view(), name="logout_view"),
]
