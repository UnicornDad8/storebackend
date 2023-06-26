from django.shortcuts import render
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    """
    collection = Collection.objects.get(pk=11)
    collection.featured_product = None
    collection.save()
    """
    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, "hello.html")
