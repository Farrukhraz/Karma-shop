from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.products, name="catalog"),
    path('catalog/category/<int:category_pk>/', views.category_items, name="category_items"),
    path('catalog/product/<int:product_pk>/', views.product_page, name="product_page"),
]
