from django.urls import path

from .apps import CatalogConfig
from .views import ProductListView, CategoryListView, ProductDetailView, CatalogListView, ContactsCreateView, \
	ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name


urlpatterns = [
		path('', ProductListView.as_view(), name='home'),
		path('contacts/', ContactsCreateView.as_view(), name='contacts'),
		path('one_product/<int:pk>', ProductDetailView.as_view(), name='one_product'),
		path('all_products/<int:pk>', CatalogListView.as_view(), name='all_products'),
		path('category/', CategoryListView.as_view(), name='category'),
		path('product/create/', ProductCreateView.as_view(), name='product_create'),
		path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
		path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
