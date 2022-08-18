from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import Movie

# Create your views here.


class MovieListView(ListView):
    template_name = 'home.html'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchTerm'] = self.request.GET.get('searchMovie')
        context['movies'] = self.object_list
        return context

    def get_queryset(self):
        query = self.request.GET.get('searchMovie')
        if query:
            return Movie.objects.filter(
                Q(title__icontains=query)
                )
        else: 
            return Movie.objects.all()

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SignUpSampleView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.GET.get('email')
        return context

