import redis
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from rest_framework.viewsets import ModelViewSet
from shortener.models import URL
from shortener.serializers import URLSerializer
from shortener.queries import get_shortened_url_all

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=settings.REDIS_DB)


class ShortenerView(ModelViewSet):
    queryset = get_shortened_url_all()
    serializer_class = URLSerializer


class RedirectOriginalURLView(View):
    def get(self, request, short_url):
        url = get_object_or_404(URL, short_url=short_url)
        redis_instance.hincrby('click_counts', short_url, 1)
        return HttpResponseRedirect(url.original_url)
