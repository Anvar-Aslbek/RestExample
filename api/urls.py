from django.urls import path
from .views import BookAPIView, BookDetailAPIViews

urlpatterns = [
    path('', BookAPIView.as_view(), name='asd'),
    path('detail/<int:pk>', BookDetailAPIViews.as_view(), name="detail")
]