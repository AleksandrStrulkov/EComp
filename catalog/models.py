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
	price = models.IntegerField(verbose_name='Цена')
	image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
	created_at = models.DateField(verbose_name='Дата создания')
	updated_at = models.DateField(auto_now=True, verbose_name='Последнее изменение')
	views_count = models.IntegerField(verbose_name='Просмотры', default=0)
	slug = models.SlugField(verbose_name='slug', max_length=150, null=True, blank=True)


	def __str__(self):
		return f'{self.name_product}{self.description_product}{self.name_category}{self.price}' \
			   f'{self.created_at}{self.updated_at}'

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


