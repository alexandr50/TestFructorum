from django.urls import path
from .apps import ComplationConfig
from .views import CreateComplationView, DeleteComplationView

app_name = ComplationConfig.name

urlpatterns = [
    path('create/', CreateComplationView.as_view(), name='create_vieew'),
    path('delete/<int:pk>/', DeleteComplationView.as_view(), name='delete_vieew'),

]
