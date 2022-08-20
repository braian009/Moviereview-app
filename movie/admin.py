from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Movie, Review

# Register your models here.


class ReviewInline(TabularInline):
    model = Review

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['title', ]
    inlines = [
        ReviewInline,
    ]

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = [
        'review',
        'movie',
        'author',
        'watchAgain',
    ]

admin.site.register(Movie, MovieAdmin)

admin.site.register(Review, ReviewAdmin)