from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm
from django.urls import reverse


def home(request):

	articles_list = Article.objects.all().order_by('-id')

	VALUES = {
		'articles_list':articles_list,
	}

	TEMPLATE = 'home.html'

	return render(request, TEMPLATE, VALUES)


def detail_page(request, id):

	article = Article.objects.get(id=id)

	VALUES = {
		'article':article,
	}

	TEMPLATE = 'detail.html'

	return render(request, TEMPLATE, VALUES)


def edit_page(request):

	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()

	VALUES = {
		'articles_list': Article.objects.all().order_by('-id'),
		'form':ArticleForm()
	}

	TEMPLATE = 'edit_page.html'

	return render(request, TEMPLATE, VALUES)


def update_page(request, id):

	success = False

	ARTICLE = Article.objects.get(id=id)

	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=ARTICLE)
		if form.is_valid():
			form.save()
			success = True

	VALUES = {
		'article':ARTICLE,
		'update':True,
		'form':ArticleForm(instance=ARTICLE),
		'success':success,
	}

	TEMPLATE = 'edit_page.html'

	return render(request, TEMPLATE, VALUES)


def delete_page(request, id):

	article = Article.objects.get(id=id)
	article.delete()

	return redirect(reverse('edit_page'))
