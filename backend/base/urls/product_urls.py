from django.urls import path
from base.views import product_views as views

urlpatterns = [
  path('', views.getProducts, name='get_products'),
  path('<str:pk>/', views.getProductDetail, name='get_product_detail'),
]