from django.urls import path
from .views import BookViewList

urlpatterns = [
    path('', BookViewList.as_view()),
]