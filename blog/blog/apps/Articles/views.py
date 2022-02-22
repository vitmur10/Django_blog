from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:7]
    return render(request, 'Articles/list.html', {'latest_articles_list': latest_articles_list})


def deteil(request, article_id):
    try:
        a = Article.objects.get(id=article_id)

    except:
        raise Http404('Статья не знайдена')

    latest_comment_list = a.comment_set.order_by('-id')[:15]

    return render(request, 'Articles/deteil.html', {'article': a,'latest_comment_list':latest_comment_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не знайдена')

    a.comment_set.create(name_user=request.POST['name'], text_comment=request.POST['text'], date_comment=timezone.now())

    return HttpResponseRedirect(reverse('Articles:deteil', args=(a.id,)))