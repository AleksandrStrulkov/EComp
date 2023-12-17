import json

from django import forms
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category, Contacts, Versions
from catalog.forms import ProductForm, VersionForm, ContactForm, VersionBaseInlineFormSet
from django.db import transaction


class ProductListView(ListView):
	model = Product
	extra_context = {
			'title': "Все товары"
	}
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		for product in context['object_list']:
			active_version = product.versions_set.filter(active_version=True).first()
			if active_version:
				product.active_version_number = active_version.number_version
				product.active_version_name = active_version.name
			else:
				product.active_version_number = None
				product.active_version_name = None
		return context


class ContactsCreateView(CreateView):
	model = Contacts
	form_class = ContactForm
	# fields = ('contact_name', 'contact_email', 'contact_text')
	success_url = reverse_lazy('catalog:contacts')
	extra_context = {
			'title': "Обратная связь"
	}

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
	paginate_by = 3


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

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)
		context_data['category'] = Category.objects.all()
		context_data['title'] = 'Создание товара'
		VersionFormSet = inlineformset_factory(self.model, Versions, form=VersionForm, extra=1)
		if self.request.method == 'POST':
			formset = VersionFormSet(self.request.POST)
		else:
			formset = VersionFormSet()

		context_data['formset'] = formset
		return context_data

	def form_valid(self, form):
		context_data = self.get_context_data()
		formset = context_data['formset']
		# with transaction.atomic():
		if form.is_valid():
			self.object = form.save()
			if formset.is_valid():
				formset.instance = self.object
				formset.save()
			else:
				return self.form_invalid(form)

		return super().form_valid(form)


class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm

	def get_success_url(self):
		return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)
		context_data['category'] = Category.objects.all()
		context_data['title'] = 'Редактирование товара'
		VersionFormSet = inlineformset_factory(
			Product, Versions, form=VersionForm, extra=1,
			formset=VersionBaseInlineFormSet
			)
		if self.request.method == 'POST':
			formset = VersionFormSet(self.request.POST, instance=self.object)
		else:
			formset = VersionFormSet(instance=self.object)

		context_data['formset'] = formset
		return context_data

	def form_valid(self, form):
		context_data = self.get_context_data()
		formset = context_data['formset']
		with transaction.atomic():
			if form.is_valid():
				self.object = form.save()
				if formset.is_valid():
					formset.instance = self.object
					formset.save()
				else:
					return self.form_invalid(form)

		return super().form_valid(form)


class ProductDeleteView(DeleteView):
	model = Product
	success_url = reverse_lazy('catalog:home')
	extra_context = {
			'title': "Удаление товара",
	}