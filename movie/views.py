from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Movie

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchTerm'] = self.request.GET.get('searchMovie')
        context['movies'] = Movie.objects.all()
        return context



class AboutPageView(TemplateView):
    template_name = 'about.html'

class SignUpSampleView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.GET.get('email')
        return context