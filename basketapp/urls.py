from django.urls import path
from basketapp import views

app_name = 'basketapp'

urlpatterns = [
    path('', views.basket, name="index"),
]
