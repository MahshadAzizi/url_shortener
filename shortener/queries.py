from shortener.models import URL


def get_shortened_url_all():
    return URL.objects.all()


def check_url_exists(shortened_url):
    if URL.objects.filter(short_url=shortened_url).exists():
        return True
    return False


def get_url_by_short_url(short_url):
    return URL.objects.filter(short_url=short_url).first()


def add_url_count_by_url(count, url: URL):
    url.click_count += count
    url.save()
    return url
