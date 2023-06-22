from django.shortcuts import render
from django.db.models import Q
from store.models import Product, Customer, Collection, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    # Products: inventory < 10 and unit price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, "hello.html", {"queryset": list(queryset)})
