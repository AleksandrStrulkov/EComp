from django.urls import path

from .apps import CatalogConfig
from .views import home, contacts, one_product, all_products, category

app_name = CatalogConfig.name


urlpatterns = [
		path('', home, name='home'),
		path('contacts/', contacts, name='contacts'),
		path('one_product/<int:pk>', one_product, name='one_product'),
		path('all_products/<int:pk>', all_products, name='all_products'),
		path('category/', category, name='category')
]
