from django.urls import path

from .apps import CatalogConfig
from .views import contacts, one_product, all_products, ProductListView, CategoryListView

app_name = CatalogConfig.name


urlpatterns = [
		path('', ProductListView.as_view(), name='home'),
		path('contacts/', contacts, name='contacts'),
		path('one_product/<int:pk>', one_product, name='one_product'),
		path('all_products/<int:pk>', all_products, name='all_products'),
		path('category/', CategoryListView.as_view(), name='category')
]
