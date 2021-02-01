from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from authapp.models import AuthPageImages, ShopUser


def send_verify_mail(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key, ])
    subject = f"Confirming {user.username} account"
    message = f"To confirm your account please follow the link:\n{settings.DOMAIN_NAME + verify_link}"
    return send_mail(
        subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email, ]
    )


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            if user.is_verified:
                print(f"User {user.username} is already verified")
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('main:index'))
            user.is_active = True
            user.is_verified = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            print(f"Couldn't verify user: {user}")
        return render(request, 'authapp/verification.html')
    except Exception as exc:
        print(f"Error occurred while activating user. Error: {exc.args}")
        return HttpResponseRedirect(reverse('main:index'))


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
            user = register_form.save()
            if send_verify_mail(user):
                print(f"Mail sent correctly to {user.username}")
            else:
                print(f"Couldn't send the mail to {user.username}")
            # user.is_active = False
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title': 'регистрация',
        'register_form': register_form,
        'auth_page_images': AuthPageImages.objects.all()
    }

    return render(request, 'authapp/register.html', content)


@transaction.atomic
def edit(request):
    if request.method == 'POST':
        update_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    content = {
        'title': 'Редактирование профиля',
        'update_form': update_form,
        'profile_form': profile_form,
        'auth_page_images': AuthPageImages.objects.all()
    }

    return render(request, 'authapp/edit.html', content)
