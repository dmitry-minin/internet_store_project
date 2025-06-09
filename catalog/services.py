from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_filtered_products(category_id):
    """
    Retrieves a list of products, optionally using cache if enabled.
    If caching is enabled, it checks the cache for the product list.
    """
    if CACHE_ENABLED:
        cache_key = f'filtered_product_list_{category_id}'
        product_list = cache.get(cache_key)
        if not product_list:
            product_list = list(Product.objects.filter(category_id=category_id).order_by('name'))
            cache.set(cache_key, product_list, timeout=60 * 15)  # Cache for 15 minutes
    else:
        product_list = list(Product.objects.filter(category_id=category_id).order_by('name'))

    return product_list
