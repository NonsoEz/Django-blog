from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def articles_index(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/articles_index.html', {'articles': articles})

def articles_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/articles_detail.html', {'article': article})

@login_required(login_url="/accounts/login/")
def articles_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:index')

    else:
        form = forms.CreateArticle()
    return render(request, 'articles/articles_create.html', {'form': form}) 