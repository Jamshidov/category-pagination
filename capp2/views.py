from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .models import *


def home(request):
    products = Product.objects.all()
    items = request.GET.get('q')

    if items:
        item = items.strip()
        products = Product.objects.filter(Q(title__icontains=item) | Q(name__icontains=item))

    paginator = Paginator(products, 2)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
        "pages": products,
    }

    return render(request, 'capp2/home.html', context)


