from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    # queryset = Product.objects.only('id', 'title')
    queryset = Product.objects.defer('description')

    return render(request, "hello.html", {"queryset": queryset})
