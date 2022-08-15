from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import HomePageView, AboutPageView, SignUpSampleView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignUpSampleView.as_view(), name='signup'),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)