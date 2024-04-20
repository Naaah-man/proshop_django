from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializers
from .models import Product
# Create your views here.

def getRoutes(request):
  return JsonResponse('Hello', safe=False)

@api_view(['GET'])
def getProducts(request):
  products = Product.objects.all()
  serializer = ProductSerializers(products, many=True)
  return Response(serializer.data)

  
@api_view(['GET'])
def getProductDetail(request, pk):
  product = Product.objects.get(_id=pk)
  serializer = ProductSerializers(product, many=False)
  return Response(serializer.data)