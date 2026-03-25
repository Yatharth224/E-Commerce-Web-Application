from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product  
from django.db.models import Q,F



def say_hello(request):
    product = Product.objects.values('id','title','collection__title   ')
    
    return render (request, 'hello.html',{'name':'Yatharth', 'products': (product) })
