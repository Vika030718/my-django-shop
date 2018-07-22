from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.db.models import Q
import datetime
from .forms import SearchForm
from .models import Product, Category



def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:8]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404("we don't have such an item:(")
    context = {'product': product}
    return render(request, 'shop/product.html', context)

def category(request, category_id):
    try:
        products_list = Product.objects.filter(category=category_id)
        category = Category.objects.get(id=category_id)
        brands = Product.objects.filter(category=category_id).values('brand').distinct('brand')
    except:
        raise Http404("we don't have such an category:(")

    form = SearchForm()

    context = {'products_list': products_list,
               'category': category,
               'brands': brands,
               'form':form,}

    return render(request, 'shop/category.html', context)


def search(request, category_id):
    try:
        products_list = Product.objects.filter(category=category_id)
        category = Category.objects.get(id=category_id)
        brands = Product.objects.filter(category=category_id).values('brand').distinct('brand')
    except:
        raise Http404("we don't have such an category:(")

    form = SearchForm()

    if request.method == 'GET':
        product_name = request.GET['product_name']
        product_price_start = request.GET['product_price_start']
        product_price_end = request.GET['product_price_end']
        p_date = request.GET['pub_date']
        product_brand = request.GET['product_brand']

        if product_name:
            products_list = products_list.filter(name__icontains=product_name)
        elif product_price_start and product_price_end:
            products_list = products_list.filter(price__range=(product_price_start, product_price_end))
        elif p_date:
            products_list = products_list.filter(pub_date=p_date)
        elif product_brand:
            products_list = products_list.filter(brand=product_brand)

    context = {'products_list': products_list,
               'category': category,
               'brands': brands,
               'form': form,}

    return render(request, 'shop/category.html', context)

def favorites(request):
    products_list = Product.objects.filter(category=1)
    context = {'products_list': products_list}
    return render(request, 'shop/favorites.html', context)
