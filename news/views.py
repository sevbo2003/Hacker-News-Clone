from django.shortcuts import render, get_object_or_404

from .models import News, Comment


def home(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)


def welcome(request):
    return render(request, 'newswelcome.html')

def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    context = {
            'item': item
    }
    return render(request, 'item_detail.html', context)


def news_link_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'item_link_detail.html', context)


def newcomments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'newcomments.html', context)