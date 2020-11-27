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
        basket_items_total_price=__get_all_items_price(basket_items),
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
    request.user.basket_set.filter(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def __get_basket_items(basket_items):
    products = Product.objects.all()
    items = []
    item = namedtuple('A', ['basket_item', 'product', 'item_total_price'])
    for basket_item in basket_items:
        try:
            product = products.filter(id=basket_item.product_id).first()
            if product:
                item_total_price = product.price * basket_item.quantity
                items.append(item(basket_item, product, item_total_price))
        except ValueError:
            continue
    return items


def __get_all_items_price(basket_items):
    total_price = 0

    for basket_item in basket_items:
        product = Product.objects.filter(id=basket_item.product_id).first()
        if product:
            try:
                product_price = float(product.price)
                if product_price > 0:
                    total_price += product_price
            except ValueError as exc:
                print(f"Incorrect product price value")
    return total_price


