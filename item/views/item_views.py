from django.shortcuts import render, get_object_or_404
from item.models import Item


def index(request):
    items = Item.objects \
        .filter(show=True)\
        .order_by('expiration_date')

    context = {
        'items': items, 
    }

    return render(
        request,
        'item/index.html',
        context
    )

def item(request, item_id):
    single_item = get_object_or_404(
        Item, pk=item_id, show=True
        )

    context = {
        'item': single_item, 
    }

    return render(
        request,
        'item/item.html',
        context
    )