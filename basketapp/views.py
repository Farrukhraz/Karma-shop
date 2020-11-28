from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product

from collections import namedtuple


@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user)

    context = dict(
        basket_items=__get_basket_items(basket_items),
        basket_items_total_price=__get_basket_items_total_price(basket_items),
    )
    return render(request, 'basketapp/basket.html', context=context)


@login_required
def basket_add(request, pk=None):

    # 1st way:
    # product = get_object_or_404(Product, pk=pk)
    # basket_item = request.user.basket_set.filter(product_id=pk).first()
    # if not basket_item:
    #     basket_item = Basket(user=request.user, product=product)

    # 2nd way:
    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        product_id=pk,
    )

    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk=None):
    print(f"Removed product from basket with id: {pk}")
    # 1st way:
    basket_item = get_object_or_404(Basket, id=pk)
    basket_item.delete()
    # 2nd way:
    # request.user.basket_set.filter(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def __get_basket_items(basket_items):
    products = Product.objects.all()
    items = []
    item = namedtuple('A', ['basket_item', 'product', 'item_total_price'])
    for basket_item in basket_items:
        try:
            product = products.filter(id=basket_item.product_id).first()
            if product:
                item_total_price = basket_item.product_cost
                items.append(item(basket_item, product, item_total_price))
        except ValueError:
            continue
    return items


def __get_basket_items_total_price(basket_items):
    total_price = sum(map(lambda x: x.product_cost, basket_items))
    return total_price
