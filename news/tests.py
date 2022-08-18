from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .models import News
from .views import NewsListView


# Create your tests here.

class NewsModelTest(TestCase):

    def setUp(self):
        self.headline = 'A nice headline'
        self.body = 'An interesting body'

        self.news = News.objects.create(
            headline = self.headline,
            body = self.body
        )

    
    def test_news_listing(self):
        self.assertEqual(f'{self.news.headline}', 'A nice headline' )

        self.assertEqual(News.objects.all().count(), 1)
        self.assertEqual(News.objects.all()[0].headline, 'A nice headline')
        self.assertEqual(News.objects.all()[0].body, 'An interesting body')

class NewsPageTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('news'))

    def test_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_page_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'news.html')
    
    def test_news_url_resolves_newslistview(self):
        view = resolve('/news/')
        self.assertEqual(view.func.__name__, NewsListView.as_view().__name__)


