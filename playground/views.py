from django.shortcuts import render
from django.db import transaction, connection
from store.models import Product, Collection, Cart, CartItem, Order, OrderItem


def say_hello(request):
    # Product.objects.raw("SELECT * FROM store_product")
    with connection.cursor() as cursor:
        cursor.execute()

    return render(request, "hello.html", {"queryset": list(queryset)})
