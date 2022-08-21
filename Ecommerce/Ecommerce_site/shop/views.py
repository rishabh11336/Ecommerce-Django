from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product


productss = Product.objects.all().values('category').distinct()


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products, 'productss': productss})


def about(request):
    return render(request, 'about.html', {'productss': productss})


def productpage(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'product.html', {'products': products, 'productss': productss})


def category(request, category):
    products = Product.objects.filter(category=category).order_by('category')
    return render(request, 'category.html', {'products': products, 'productss': productss})

def search(request):
    q=request.GET['q']
    data1 = Product.objects.filter(tag=q).order_by('-id')
    data2 = Product.objects.filter(name=q).order_by('-id')
    if data1:
        data = data1
    else:
        data = data2
    print(data)
    print(data2)
    return render(request, 'Search.html', {'productss': productss, 'data':data})


def Cart(request):
    return render(request, 'cart.html', {'productss': productss})