from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index, name='karma_main_page_index'),
]
