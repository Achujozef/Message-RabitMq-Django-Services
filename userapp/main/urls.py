from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/<int:id>/like/', views.like_product, name='like_product'),
]
