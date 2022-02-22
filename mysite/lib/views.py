from django.shortcuts import render

# Create your views here.
from .models import Authors


def index(request):
    author = Authors.objects.all()
    context = {'author': author}
    return render(request, 'lib/defoult.html', context)

def ganre(request):
    author = Authors.objects.all()
    context = {'author': author}
    return render(request, 'lib/ganre.html', context)
def book(request):
    author = Authors.objects.all()
    context = {'author': author}
    return render(request, 'lib/book.html', context)