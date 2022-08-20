from django.urls import path

from .views import MovieListView, MovieDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('<int:pk>/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>', ReviewUpdateView.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
] 