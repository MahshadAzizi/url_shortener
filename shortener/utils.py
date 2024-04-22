from shortener.queries import check_url_exists, get_url_by_short_url, add_url_count_by_url


def update_urls_count(data: dict):
    for key, value in data.items():
        if check_url_exists(key):
            url_obj = get_url_by_short_url(key)
            add_url_count_by_url(count=int(value), url=url_obj)



