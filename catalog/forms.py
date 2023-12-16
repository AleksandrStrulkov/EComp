from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name_product', 'description_product', 'name_category', 'price', 'image', 'created_at',)


