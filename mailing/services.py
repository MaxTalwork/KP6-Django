from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_prod_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    prod = cache.get(key)
    if prod is not None:
        return prod
    prod = Product.objects.all()
    cache.set(key, prod)
    return prod