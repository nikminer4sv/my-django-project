from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = "__all__"

	def __init__(self, *args, **kwarg):
		super().__init__(*args, **kwarg)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'