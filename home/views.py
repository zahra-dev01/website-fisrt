from django.shortcuts import render
from .models import *


def home(request):
    category = Category.objects.all()
    return render(request, 'home/home.html', {'category':category})


def all_product(request):
    return render(request, 'home/product.html')