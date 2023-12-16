from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name_product', 'description_product', 'name_category', 'price', 'created_at',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	def clean_name_product(self):
		cleaned_data = self.cleaned_data['name_product']
		forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
							'полиция', 'радар']

		for obj in forbidden_words:
			if obj in cleaned_data:
				raise forms.ValidationError("Продукт запрещен в нашем магазине")

		return cleaned_data

	def clean_description_product(self):
		cleaned_data = self.cleaned_data['description_product']
		forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
							'полиция', 'радар']

		for obj in forbidden_words:
			if obj in cleaned_data:
				raise forms.ValidationError("В описании присутствуют запрещенные слова")

		return cleaned_data
