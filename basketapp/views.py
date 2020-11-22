from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    return render(request, 'basketapp/basket.html')


def basket_add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    basket_item = request.user.basket_set.filter(product_id=pk).first()
    if not basket_item:
        basket_item = Basket(user=request.user, product=product)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk=None):
    print(f"Removed product pk: {pk}")
