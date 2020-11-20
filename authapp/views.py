from django.shortcuts import render
from authapp.forms import ShopUserLoginForm
from authapp.models import AuthPageImages
from mainapp.models import Product


def login(request):
    form = ShopUserLoginForm()
    context = dict(
        form=form,
        auth_page_images=AuthPageImages.objects.all(),
        product=Product.objects.all()
    )
    auth_page = context.get("auth_page_images")[0].image.url
    return render(request, 'authapp/login.html', context=context)
