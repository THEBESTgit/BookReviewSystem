from rest_framework import viewsets
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book, User, Review
from .serializers import AuthorSerializer, BookSerializer, UserSerializer, ReviewSerializer
from django.shortcuts import render

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Custom API
@api_view(['GET'])
def top_rated_books(request):
    books = Book.objects.annotate(avg_rating=Avg('reviews__rating')).filter(avg_rating__gt=4).order_by('-avg_rating')
    serialized_books = [
        {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "published_date": book.published_date,
            "author": book.author.name,
            "average_rating": book.avg_rating
        }
        for book in books
    ]

    # Cambiar 'serializer' por 'serialized_books'
    return Response(serialized_books)

def book_list(request):
    books = Book.objects.all() 
    return render(request, 'books/book_list.html', {'books': books})

