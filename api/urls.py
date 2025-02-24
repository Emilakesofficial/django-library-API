from django.urls import path
from .views import BookAPIView, BookAPIDetailView

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('', BookAPIDetailView.as_view())
]