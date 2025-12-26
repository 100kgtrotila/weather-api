import redis
from config import REDIS_PASSWORD, REDIS_PORT, REDIS_HOST

def get_cache():
    try:
        cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
        cache.ping()
        return cache
    except redis.exceptions.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
