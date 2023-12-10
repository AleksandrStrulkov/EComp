from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
	title = models.CharField(max_length=50, verbose_name='Заголовок')
	slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
	body = models.TextField(verbose_name='Содержимое')
	image = models.ImageField(upload_to='images_blog/', verbose_name='Изображение', **NULLABLE)
	updated_at = models.DateField(auto_now=True, verbose_name='Последнее изменение')
	is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
	views_count = models.IntegerField(verbose_name='просмотры', default=0)


	def __str__(self):
		return f'{self.title} - {self.slug}'

	class Meta:
		verbose_name = 'блог'
		verbose_name_plural = 'блоги'


