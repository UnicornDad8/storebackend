from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, OrderItem


def say_hello(request):
    # queryset = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

    # How many orders do we have?
    # queryset = Order.objects.aggregate(count=Count("id"))

    # How many units of product 1 have we sold?
    # queryset = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Sum("quantity"))

    # How many orders has customer 1 placed?
    # queryset = Order.objects.filter(customer__id=1).aggregate(count=Count("id"))

    # What is the min, max and avg price of products in collection 1?
    queryset = Product.objects.filter(collection__id=3).aggregate(min_price=Min(
        "unit_price"), avg_price=Avg("unit_price"), max_price=Max("unit_price"))

    return render(request, "hello.html", {"queryset": queryset})
