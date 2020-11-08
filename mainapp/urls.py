from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.category, name="index"),
    path('<int:pk>/', views.category, name="category"),
]
