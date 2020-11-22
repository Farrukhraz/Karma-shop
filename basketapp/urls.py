from django.urls import path
from basketapp import views

app_name = 'basketapp'

urlpatterns = [
    path('', views.basket, name="index"),
    path('add/<int:pk>/', views.basket_add, name="add"),
    path('remove/<int:pk>/', views.basket_remove, name="remove"),
]
