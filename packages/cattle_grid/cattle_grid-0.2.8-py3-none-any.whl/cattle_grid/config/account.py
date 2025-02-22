from functools import lru_cache
from .settings import get_settings


@lru_cache
def get_base_urls():
    return get_settings().frontend.base_urls
