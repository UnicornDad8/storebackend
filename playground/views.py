from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    # select_related(1)
    # queryset = Product.objects.select_related('collection').all()
    # prefetch_related(n)
    # queryset = Product.objects.prefetch_related('promotions').select_related("collection").all()

    # Exercise: Get the last 5 orders with their customer and items (including product)
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, "hello.html", {"queryset": queryset})
