import json

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category, Contacts
from pytils.translit import slugify

# def home(request):
# 	product_item = Product.objects.all()
# 	context = {
# 			'object_list': product_item,
# 			'title': 'Все товары'
# 	}
# 	return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
	model = Product
	extra_context = {
			'title': "Все товары"
	}


# def contacts.json(request):
# 	if request.method == 'POST':
# 		# в переменной request хранится информация о методе, который отправлял пользователь
# 		name = request.POST.get('name')
# 		phone = request.POST.get('phone')
# 		message = request.POST.get('message')
# 		# а также передается информация, которую заполнил пользователь
# 		print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')
# 	context = {
# 			'title': 'Контакты'
# 		}
# 	return render(request, 'catalog/contacts_form.html', context)


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




# def one_product(request, pk):
# 	product_item = Product.objects.get(pk=pk)
# 	context = {
# 			'object_list': product_item,
# 			'title': f'{product_item.name_product}'
# 	}
# 	return render(request, 'catalog/product_detail.html', context)


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
	


# def category(request):
# 	context = {
# 			'object_list': Category.objects.all(),
# 			'title': 'Категории товаров'
# 	}
# 	return render(request, 'catalog/category_list.html', context)


class CategoryListView(ListView):
	model = Category
	extra_context = {
			'title': "Категории товаров"
	}

# def all_products(request, pk):
# 	category_item = Category.objects.get(pk=pk)
# 	context = {
# 			'object_list': Product.objects.filter(name_category_id=pk),
# 			'title': f'{category_item.name_category}'
# 	}
# 	return render(request, 'catalog/catalog_list.html', context)


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

