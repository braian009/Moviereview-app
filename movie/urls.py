from django.urls import path

from .views import MovieListView, AboutPageView, SignUpSampleView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignUpSampleView.as_view(), name='signup'),
] 