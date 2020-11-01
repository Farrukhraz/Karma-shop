import os
import json
from django.shortcuts import render
from karma.settings import BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, 'data', 'mainapp')


def index(request):
    with open(os.path.join(DATA_DIR, 'index.json')) as f:
        context = json.load(f)
    return render(request, 'mainapp/index.html', context=context)


def category(request):
    with open(os.path.join(DATA_DIR, 'category.json')) as f:
        context = json.load(f)
    return render(request, 'mainapp/category.html', context=context)


def single_product(request):
    with open(os.path.join(DATA_DIR, 'single-product.json')) as f:
        context = json.load(f)
    return render(request, 'mainapp/single-product.html', context=context)
