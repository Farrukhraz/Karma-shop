from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index, name='karma_main_page_index'),
    path('single-product.html/', views.single_product, name="single-product"),
    path('category.html/', views.category, name="category"),
]
