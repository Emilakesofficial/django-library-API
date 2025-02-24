from django.shortcuts import render
from rest_framework.views import APIView
from books.models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import serializers, status

class BookAPIView(APIView):
    def get(self, request):
        try:
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class BookAPIDetailView(APIView):
    def get(self, request, id):
        try:
            book = Book.object.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book, instance=book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, id):
        try: 
            book = Book.objects.get(id=id)
            book.delete()
            return Response(f"{self.title} deleted successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)