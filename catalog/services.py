from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from catalog.models import Category


def cached_category():
    if settings.CASH_ENABLE:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list, 60)
    else:
        category_list = Category.objects.all()
    return category_list
