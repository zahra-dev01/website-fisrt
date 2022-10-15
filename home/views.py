from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Variants, Comment, CommentForm, ReplyForm, Images
from .forms import SearchForm
from django.db.models import Q
from Cart.models import *


def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
    products = Product.objects.all()
    form = SearchForm()
    category = Category.objects.filter(sub_cat=False)
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            products = products.filter(Q(name__contains=data))
    if slug and id:
        data = get_object_or_404(Category, slug=slug, id=id)
        products = Product.objects.filter(category=data)
    return render(request, 'home/product.html', {'products': products, 'category': category, 'form': form})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    images = Images.objects.filter(product_id= id)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    cart_form = CartForm()
    comment_show = Comment.objects.filter(product_id=id, is_reply=False)
    similar = product.tags.similar_objects()[:10]
    is_like = False
    if product.like.filter(id=request.user.id).exists():
        is_like = True
    is_unlike = False
    if product.unlike.filter(id=request.user.id).exists():
        is_unlike = True
    if product.status != 'None':
        if request.method == 'POST':
            variant = Variants.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variants.objects.get(id=var_id)
        else:
            variant = Variants.objects.filter(product_variant_id=id)
            variants = Variants.objects.get(id=variant[0].id)
        context = {'product': product, 'variant': variant, 'variants': variants, 'similar': similar, 'is_like': is_like,
                   'is_unlike': is_unlike, 'comment_form': comment_form, 'comment_show': comment_show,
                   'reply_form':reply_form, 'images': images, 'cart_form': cart_form}
        return render(request, 'home/detail.html', context)
    else:
        return render(request, 'home/detail.html', {'product': product, 'similar': similar, 'is_like': is_like,
                                                    'is_unlike': is_unlike, 'comment_show': comment_show,
                                                    'reply_form': reply_form, 'images': images, 'cart_form': cart_form})


def product_like(request, id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, id=id)
    is_like = False
    if product.like.filter(id=request.user.id).exists():
        product.like.remove(request.user)
        is_like = False
    else:
        product.like.add(request.user)
        is_like = True
    return redirect(url)


def product_unlike(request, id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, id=id)
    is_unlike = False
    if product.unlike.filter(id=request.user.id).exists():
        product.unlike.remove(request.user)
        is_unlike = False
    else:
        product.unlike.add(request.user)
        is_unlike = True
    return redirect(url)


def product_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'], rate=data['rate'], user_id=request.user.id, product_id=id)
            return redirect(url)
        else:
            return redirect(url)


def product_reply(request, id, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = reply_form.cleaned_data
            Comment.objects.create(comment=data['comment'], product_id=id, user_id=request.user.id,
                                   reply_id=comment_id, is_reply=True)
            return redirect(url)


def comment_like(request, id):
    url = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(id=id)
    if comment.comment_like.filter(id=request.user.id).exists():
        comment.comment_like.remove(request.user)
    else:
        comment.comment_like.add(request.user)
    return redirect(url)


def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data.isdigit():
                products = products.filter(Q(discount__exact=data) | Q(unit_price__exact=data))
            else:
                products = products.filter(Q(name__contains=data))
            return render(request, 'home/product.html', {'products': products, 'form': form})



