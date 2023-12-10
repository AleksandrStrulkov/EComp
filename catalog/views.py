from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Category
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


def contacts(request):
	if request.method == 'POST':
		# в переменной request хранится информация о методе, который отправлял пользователь
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		# а также передается информация, которую заполнил пользователь
		print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')
	context = {
			'title': 'Контакты'
		}
	return render(request, 'catalog/contacts.html', context)


def one_product(request, pk):
	product_item = Product.objects.get(pk=pk)
	context = {
			'object_list': product_item,
			'title': f'{product_item.name_product}'
	}
	return render(request, 'catalog/one_product.html', context)


def category(request):
	context = {
			'object_list': Category.objects.all(),
			'title': 'Категории товаров'
	}
	return render(request, 'catalog/category_list.html', context)


class CategoryListView(ListView):
	model = Category
	extra_context = {
			'title': "Категории товаров"
	}


def all_products(request, pk):
	category_item = Category.objects.get(pk=pk)
	context = {
			'object_list': Product.objects.filter(name_category_id=pk),
			'title': f'{category_item.name_category}'
	}
	return render(request, 'catalog/all_products.html', context)



