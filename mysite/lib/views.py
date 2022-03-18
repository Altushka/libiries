from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    author = Authors.objects.all()  #select_related(id)
    book = Books.objects.all()
    context = {'author': author,'books': book}
    return render(request, 'lib/defoult.html', context)

def ganre(request):
    ganre = Genres.objects.select_related(id)
    context = {'ganre': ganre}
    return render(request, 'lib/ganre.html', context)

def author(request,author_id):
    author = Authors.objects.get(pk=author_id)
    books = Books.objects.select_related(author_id) # ошибка выбора книг
    context =  {'author': author,'books': books}
    return render(request, 'lib/author.html', context)

def books(request,book_id):
    book = Books.objects.get(pk=book_id)
    context = {'book':book}
    return render(request, 'lib/book.html', context)


