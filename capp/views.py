from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Category


def homepage(request):
    items = Product.objects.all()
    categories = Category.objects.all()

    page = request.GET.get('page')
    pg = Paginator(items, 2)

    try:
        pages = pg.page(page)
    except PageNotAnInteger:
        pages = pg.page(1)
    except EmptyPage:
        pages = pg.page(pg.num_pages)

    context = {
        "items": items,
        "categories": categories,
        "pages": pages,
    }
    return render(request, 'capp/index.html', context)


def category_block(request, slug):
    items = Product.objects.filter(category__slug=slug)
    categories = Category.objects.all()

    pg = Paginator(items, 2)
    page = request.GET.get('page')

    try:
        items = pg.page(page)
    except PageNotAnInteger:
        items = pg.page(1)
    except EmptyPage:
        items = pg.page(pg.num_pages)

    context = {
        "items": items,
        "pages": items,
        "categories": categories,
        "pg": pg,
    }
    return render(request, 'capp/index.html', context)


def product_detail(request, id, slug):
    items = Product.objects.filter(slug=slug, id=id)
    context = {
        "items": items,
    }
    return render(request, 'capp/detail.html', context)
