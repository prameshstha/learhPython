from django.urls import path
from .views import (PostListAPIView,
                    PostDetailAPIView,
                    PostDeleteAPIView,
                    PostUpdateAPIView,
                    PostCreateAPIView
                    )

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='details'),
    path('edit/<int:pk>/', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteAPIView.as_view(), name='delete'),


]
