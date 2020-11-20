from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm
from authapp.models import AuthPageImages


def login(request):
    if request.method == "POST":
        # authenticate
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            user_name = request.POST.get('username')
            password = request.POST.get("password")
            user = auth.authenticate(username=user_name, password=password)
            if user and user.is_active:
                auth.login(request, user)   # cookie creation
                return HttpResponseRedirect(reverse('main'))
    else:
        # render empty form
        form = ShopUserLoginForm()
    context = dict(
        form=form,
        auth_page_images=AuthPageImages.objects.all()
    )
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))