from django.urls import path

from .apps import CatalogConfig
from .views import contacts, all_products, ProductListView, CategoryListView, ProductDetailView

app_name = CatalogConfig.name


urlpatterns = [
		path('', ProductListView.as_view(), name='home'),
		path('contacts/', contacts, name='contacts'),
		path('one_product/<int:pk>', ProductDetailView.as_view(), name='one_product'),
		path('all_products/<int:pk>', all_products, name='all_products'),
		path('category/', CategoryListView.as_view(), name='category')
]
