from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.serializers import ProductSerializers
from base.models import Product

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