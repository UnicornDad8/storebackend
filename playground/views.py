from django.shortcuts import render
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection.objects.get(pk=11)
    collection.delete()

    Collection.objects.filter(id__gt=5).delete()

    return render(request, "hello.html")
