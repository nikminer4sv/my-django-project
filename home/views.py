from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
import wikipedia as wp


def wikipediaFunc(r):
    wp.set_lang('ru')
    result = ''

    try:
        text = wp.summary(r)
        resText = ""
        for x in text:
            if x == '\n':
                break
            else:
                resText += x
        return resText
    except wp.exceptions.DisambiguationError as e:
        for x in e.options:
            if (not x.capitalize() == r) and (not x.lower() == r):
                result += x + ' '
        return result
    except wp.exceptions.PageError as e:
        return "Страница не найдена!"


def home(request):

	articles_list = Article.objects.all().order_by('-id')

	date = {}

	for x in articles_list:
		day = x.create_date.day
		if int(day) < 10:
			day = '0' + str(day)
		month = x.create_date.month
		if int(month) < 10:
			day = '0' + str(month)
		date[x] = '{}.{}.{}'.format(day, month, x.create_date.year)


	VALUES = {
		'articles_list':articles_list,
		'date':date
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

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'edit_page.html'
	form_class = ArticleForm
	success_url = reverse_lazy('edit_page')

	def get_context_data(self, **kwargs):
		kwargs['articles_list'] = Article.objects.all().order_by('-id')
		return super().get_context_data(**kwargs)


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


def wiki(request):

	TEMPLATE = 'wiki.html'

	VALUES = {'wikiTextField':''}

	try:
		VALUES['wikiTextField'] = request.GET['wikiTextField']
		VALUES['response'] = wikipediaFunc(VALUES['wikiTextField'])
	except:
		pass


	return render(request, TEMPLATE, VALUES)















"""
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
"""
