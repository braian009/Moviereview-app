from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    watchAgain = models.BooleanField()

    
    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.movie.id)])
    


