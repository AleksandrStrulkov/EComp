import json

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category, Contacts
from catalog.forms import ProductForm


class ProductListView(ListView):
	model = Product
	extra_context = {
			'title': "Все товары"
	}


class ContactsCreateView(CreateView):
	model = Contacts
	fields = ('contact_name', 'contact_email', 'contact_text')
	success_url = reverse_lazy('catalog:contacts')

	def form_valid(self, form):
		if form.is_valid():
			new_contact = form.save()
			new_contact.personal_manager = self.request.user
			new_contact.save()
			contact_dict = {
				"Имя": new_contact.contact_name,
				"Почта": new_contact.contact_email,
				"Сообщение": new_contact.contact_text,
			}
			with open("contacts.json", 'a', encoding='UTF-8') as f:
				json.dump(contact_dict, f, indent=2, ensure_ascii=False)

		return super().form_valid(form)


class ProductDetailView(DetailView):
	model = Product

	def get_object(self, queryset=None):
		self.object = super().get_object(queryset)
		self.object.views_count += 1
		self.object.save()
		return self.object

	def get_context_data(self, *args, **kwargs):
		context_data = super().get_context_data(*args, **kwargs)

		product_item = Product.objects.get(pk=self.kwargs.get('pk'))
		context_data['title'] = f'{product_item.name_product}'

		return context_data


class CategoryListView(ListView):
	model = Category
	extra_context = {
			'title': "Категории товаров",
	}


class CatalogListView(ListView):
	model = Product

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.filter(name_category_id=self.kwargs.get('pk'))
		return queryset

	def get_context_data(self, *args, **kwargs):
		context_data = super().get_context_data(*args, **kwargs)

		category_item = Category.objects.get(pk=self.kwargs.get('pk'))
		context_data['category_pk'] = category_item.pk
		context_data['title'] = f'{category_item.name_category}'

		return context_data


class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm
	success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm
	success_url = reverse_lazy('catalog:home')

class ProductDeleteView(DeleteView):
	model = Product
	success_url = reverse_lazy('catalog:home')



