from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='karma_main_page_index'),
    path('single-product.html/', views.single_product, name="single_product"),
    path('category.html/', views.category, name="category"),
]
