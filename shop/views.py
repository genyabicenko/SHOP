from django.shortcuts import render, get_object_or_404
from haystack.query import SearchQuerySet
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q
from django.views.generic import ListView, DetailView

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render (request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', context={
        'product': product,
        'cart_product_form': cart_product_form,
    }) 

def search(request):
    query = request.GET.get('q')
    results = SearchQuerySet().filter(content=query)
    return render(request, 'shop/product/search.html', {'results': results})

def filter_by_price(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products = Product.objects.filter(price__range=(min_price, max_price))
    return render(request, 'shop/product/list.html', {'products': products})


