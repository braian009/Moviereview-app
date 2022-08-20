from django.shortcuts import render
from django.views.generic import ListView

from .models import News

# Create your views here.

class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news/news_list.html'
    ordering = ['-date']
    