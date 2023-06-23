from django.shortcuts import render
from django.db.models import Value, Max, F, Count, Sum, ExpressionWrapper, DecimalField
from store.models import Product, Customer, Collection


def say_hello(request):
    # Annotating exercises:

    # Customers and their las order id
    """
    queryset = Customer.objects.annotate(
        last_order_id=Max("order__id")
    )
    """

    # Collections and count of their products
    # queryset = Collection.objects.annotate(products_count=Count("product"))

    # Customers with more than 5 orders
    """
    queryset = Customer.objects.annotate(
        orders_count=Count("order")
    ).filter(orders_count__gt=5)
    """

    # Customers and the total ammount they've spent
    """
    queryset = Customer.objects.annotate(
        total_spent=Sum(
            F("order__orderitem__unit_price") *
            F("order__orderitem__quantity"))
    )
    """

    # Top 5 best-selling products and their total sales
    queryset = Product.objects.annotate(
        total_sales=Sum(
            F("orderitem__unit_price") *
            F("orderitem__quantity"))
    ).order_by("-total_sales")[:5]

    return render(request, "hello.html", {"queryset": list(queryset)})
