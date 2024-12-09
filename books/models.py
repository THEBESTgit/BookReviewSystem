from django.db import models
from django.core.exceptions import ValidationError

# Validación personalizada
def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError("El puntaje debe estar entre 1 y 5.")

# Modelo de Autor
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Modelo de Libro
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Modelo de Usuario
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

# Modelo de Reseña
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[validate_rating])  # Validación personalizada
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review de {self.user.username} para {self.book.title}"
