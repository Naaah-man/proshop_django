from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes, name='routes'),
  path('products/', views.getProducts, name='get_products'),
  path('product/<str:pk>/', views.getProductDetail, name='get_product_detail'),
]