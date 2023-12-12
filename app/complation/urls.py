from django.urls import path
from .apps import ComplationConfig
from .views import CreateComplationView, DeleteComplationView, UpdateComplationView

app_name = ComplationConfig.name

urlpatterns = [
    path('create/', CreateComplationView.as_view(), name='create_view'),
    path('update/<int:pk>/', UpdateComplationView.as_view(), name='update_view'),
    path('delete/<int:pk>/', DeleteComplationView.as_view(), name='delete_view'),
]
