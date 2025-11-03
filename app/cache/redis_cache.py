import json
import redis
# from app.core.config import settings

# redis_client = redis.Redis.from_url(settings.REDIS_URL)

# def get_cached_prediction(key:str):
#     value = redis_client.get(key)
#     if value:
#         return json.loads(value)
#     return None

# def set_cache_prediction(key: str, value:dict, expiry:int=3600):
#     redis_client.setex(key, expiry, json.dumps(value))

from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

def get_cached_prediction(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache_prediction(key: str, value: dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))
