from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
    products = Product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = get_object_or_404(Category, slug=slug, id=id)
        products = Product.objects.filter(category=data)
    return render(request, 'home/product.html', {'products': products, 'category': category})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'home/detail.html', {'product': product})

