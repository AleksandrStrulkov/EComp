from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Product, Versions, Contacts, StatusProduct


class StyleFormMixin:
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name_product', 'description_product', 'name_category', 'image', 'price', 'created_at',)

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


class VersionForm(forms.ModelForm):
	class Meta:
		model = Versions
		# exclude = ('product',)
		fields = ('number_version', 'name', 'active_version')
		widgets = {
				'number_version': forms.Select(attrs={'class': 'form-control'}),
				'name': forms.Select(attrs={'class': 'form-control'}),
				'active_version': forms.NullBooleanSelect(attrs={'class': 'form-control'}),

		}


class ContactForm(StyleFormMixin, forms.ModelForm):
	class Meta:
		model = Contacts
		fields = ('contact_name', 'contact_email', 'contact_text',)


class VersionBaseInlineFormSet(BaseInlineFormSet):
	def clean(self):
		super().clean()
		active_list = [form.cleaned_data['active_version'] for form in self.forms if 'active_version' in
						form.cleaned_data]
		if active_list.count(True) > 1:
			print("У продукта возможна только одна активная версия!")
			raise forms.ValidationError("У продукта возможна только одна активная версия!")


class ProductModeratorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field_name != 'is_published':
				field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Product
		fields = ('is_published', 'description_product', 'name_category',)

