from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
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
                return HttpResponseRedirect(reverse('main:index'))
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
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title': 'регистрация',
        'register_form': register_form,
        'auth_page_images': AuthPageImages.objects.all()
    }

    return render(request, 'authapp/register.html', content)


def edit(request):
    if request.method == 'POST':
        update_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = ShopUserEditForm(instance=request.user)

    content = {
        'title': 'Редактирование профиля',
        'update_form': update_form,
        'auth_page_images': AuthPageImages.objects.all()
    }

    return render(request, 'authapp/edit.html', content)
