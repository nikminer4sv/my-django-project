from django.db import models

class Article(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	name = models.CharField('Название', max_length=200)
	text = models.TextField('Текст')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Статью'
		verbose_name_plural = 'Статьи'
