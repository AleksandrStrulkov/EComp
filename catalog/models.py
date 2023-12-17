from django.db import models
from django.db import connection

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
	name_category = models.CharField(max_length=100, verbose_name='Категория')
	description_category = models.TextField(verbose_name='Описание', **NULLABLE)
	image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

	def __str__(self):
		return f'{self.name_category}'

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;')


class Product(models.Model):
	name_product = models.CharField(max_length=100, verbose_name='Наименование')
	description_product = models.TextField(verbose_name='Описание', **NULLABLE)
	name_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')
	image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
	created_at = models.DateField(verbose_name='Дата создания')
	updated_at = models.DateField(auto_now=True, verbose_name='Последнее изменение')
	views_count = models.IntegerField(verbose_name='Просмотры', default=0)
	slug = models.SlugField(verbose_name='slug', max_length=150, null=True, blank=True)


	def __str__(self):
		return f'{self.name_product}'

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;')


class Contacts(models.Model):
	contact_name = models.CharField(max_length=30, verbose_name='Ваше имя')
	contact_email = models.CharField(max_length=30, verbose_name='Ваш email')
	contact_text = models.TextField(verbose_name='Ваше сообщение', default='Cпасибо')

	def __str__(self):
		return f'{self.contact_name} - {self.contact_email}'

	class Meta:
		verbose_name = 'контакт'
		verbose_name_plural = 'контакты'
		ordering = ('contact_name',)


class Versions(models.Model):
	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
	number_version = models.ForeignKey('NumberVersion', on_delete=models.CASCADE, verbose_name='номер версии')
	name = models.ForeignKey('StatusProduct', on_delete=models.CASCADE, verbose_name='наименование')
	active_version = models.BooleanField(verbose_name='признак версии')

	def __str__(self):
		return f'{self.name}, {self.number_version}'

	class Meta:
		verbose_name = 'версия'
		verbose_name_plural = 'версии'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_version_id_seq RESTART WITH 1;')


class StatusProduct(models.Model):
	status_name = models.CharField(max_length=150, verbose_name='статус товара на складе', unique=True)

	def __str__(self):
		return f'{self.status_name}'

	class Meta:
		verbose_name = 'статус'
		verbose_name_plural = 'статусы'


class NumberVersion(models.Model):
	status_name = models.IntegerField(verbose_name='номер версии', unique=True)

	def __str__(self):
		return f'{self.status_name}'

	class Meta:
		verbose_name = 'номер версии'
		verbose_name_plural = 'номера версии'
