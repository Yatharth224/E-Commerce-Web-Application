"""

from django.shortcuts import render  
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import  Product  ,Customer
  




def say_hello(request):

    queryset = Customer.objects.annotate(is_new=True)
     
    




    return render(request, 'hello.html', {'name': 'Yatharth', 'result': list(queryset)})"""









from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Cart, Cart_item
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/detail.html', {'product': product})


def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'collections/list.html', {'collections': collections})

def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'collections/list.html', {'collections': collections})


def collection_detail(request, id):
    collection = get_object_or_404(Collection, pk=id)
    products = Product.objects.filter(collection=collection)
    return render(request, 'collections/detail.html', {
        'collection': collection,
        'products': products
    })


def create_cart(request):
    cart = Cart.objects.create()
    return JsonResponse({'cart_id': cart.id})


def add_to_cart(request, cart_id, product_id):
    cart_item, created = Cart_item.objects.get_or_create(