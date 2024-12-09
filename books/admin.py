from django.contrib import admin
from .models import Author, Book, Review, User

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'comment')  # Campos visibles en la lista
    search_fields = ('rating', 'comment', 'book__title', 'user__username') 
admin.site.register(Review, ReviewAdmin)

