from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders_list, name='orders'),
    path('products/', views.products_list, name='products'),
]