from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login, name="login"),
]
