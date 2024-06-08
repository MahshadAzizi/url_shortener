from celery import shared_task
import redis
from django.conf import settings

from shortener.utils import update_urls_count

# Connect to Redis
redis_conn = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


@shared_task
def process_redis_data():
    data = redis_conn.hgetall('click_counts')
    if data:
        important_data = {k.decode(): int(v.decode()) for (k, v) in data.items()}
        update_urls_count(important_data)
        reset_important_data_keys(important_data)
        print("Data retrieved from Redis:", data)
    else:
        print("No data found in Redis.")


def reset_important_data_keys(important_data):
    # Iterate over the keys in the important data
    for key in important_data.keys():
        # Set the value of each key to zero
        redis_conn.hset('click_counts', key, 0)
