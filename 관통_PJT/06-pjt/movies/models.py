from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    GENRE_CHOICES = [
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Horror', 'Horror'),
    ]
    title = models.CharField(max_length=200)
    summary = models.TextField()
    director = models.CharField(max_length=100)
    director_img_url = models.URLField(null=True, blank=True) 
    director_info = models.TextField(null=True, blank=True)    
    director_works = models.TextField(null=True, blank=True)   
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    
    
    def __str__(self):
        return f"{self.title} ({self.genre})"
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
