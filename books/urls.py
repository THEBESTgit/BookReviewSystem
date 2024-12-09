from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import book_list, BookViewSet

from . import views
from .views import AuthorViewSet, BookViewSet, UserViewSet, ReviewViewSet, top_rated_books

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)

router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'books', BookViewSet, basename='book')
urlpatterns = [
    path('books/html/', book_list, name='book-list-html'),
    path('books/top-rated/', top_rated_books, name='top-rated-books'),  
]


urlpatterns += router.urls
