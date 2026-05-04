"""

from django.shortcuts import render  
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import  Product  ,Customer
  




def say_hello(request):

    queryset = Customer.objects.annotate(is_new=True)
     
    




    return render(request, 'hello.html', {'name': 'Yatharth', 'result': list(queryset)})"""









from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

