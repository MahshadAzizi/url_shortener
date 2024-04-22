from django.urls import path
from shortener.views import ShortenerView, RedirectOriginalURLView

urlpatterns = [
    path('', ShortenerView.as_view({
        'post': 'create'
    }), name='shortener'),
    path('<str:short_url>/', RedirectOriginalURLView.as_view(), name='redirect-original-url'),

]
