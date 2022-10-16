from unicodedata import category
from django.shortcuts import render
import datetime
from .models import Category,Article
from fallowers.models import Fallower
from django.contrib.auth.models import User

# Create your views here.

def function(request):
    articles = Article.objects.all()
    print(articles)
    categories = Category.objects.all()
    context = {"articles":articles, "categories":categories}

    return render(request, "index.html", context)
    

def article_detail(request,article_id):
    a = Article.objects.get(id=article_id)
    pass

def category_articles(request,category_id):
    category = Category.objects.get(id=category_id)
    a = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {"articles":a, "categories":categories}
    return render(request, "index.html", context)

