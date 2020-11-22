from django.shortcuts import render


def basket(request):
    return render(request, 'basketapp/basket.html')

    # if request.method == 'POST':
    #     register_form = ShopUserRegisterForm(request.POST, request.FILES)
    #
    #     if register_form.is_valid():
    #         register_form.save()
    #         return HttpResponseRedirect(reverse('auth:login'))
    # else:
    #     register_form = ShopUserRegisterForm()
    #
    # content = {
    #     'title': 'регистрация',
    #     'register_form': register_form,
    #     'auth_page_images': AuthPageImages.objects.all()
    # }
    #
    # return render(request, 'authapp/register.html', content)
