from django.urls import path
from .apps import BookmarkConfig
from .views import CreateBookmarkView, DeleteBookmarkView, AddBookmarkToComplationView

app_name = BookmarkConfig.name

urlpatterns = [
    path('create/', CreateBookmarkView.as_view(), name='create_vieew'),
    path('delete/<int:pk>/', DeleteBookmarkView.as_view(), name='delete_vieew'),
    path('update/<int:pk>/', AddBookmarkToComplationView.as_view(), name='update_vieew'),

]
