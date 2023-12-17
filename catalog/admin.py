from django.contrib import admin
from catalog.models import Product, Category, Versions, StatusProduct


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'name_category', 'created_at', 'updated_at')
    list_filter = ('name_category',)
    search_fields = ('name_product', 'description_product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Versions)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_version', 'name', 'active_version')
    list_filter = ('product', )


@admin.register(StatusProduct)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
