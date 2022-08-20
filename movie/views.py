from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Review

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(id = self.kwargs['pk'])
        movie = Movie.objects.get(id = self.kwargs['pk'])
        context['reviews'] = Review.objects.filter(movie = movie)
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('review', 'watchAgain',)
    template_name = 'review_create.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = get_object_or_404(Movie, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        form.instance.movie = get_object_or_404(Movie, pk = self.kwargs['pk'])
        return super().form_valid(form)

    login_url = 'account_login'

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['review']
    template_name = 'review_edit.html'
    login_url = 'account_login'

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review

    def get_success_url(self):
        return reverse_lazy('movie_detail', args=[str(self.object.movie.id)])

    login_url = 'account_login'

    

        

    

