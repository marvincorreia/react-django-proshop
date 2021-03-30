from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . import models
from . import serializers

@api_view(['GET'])
def getRoutes(request):
  return Response(['/api/products'])


@api_view(['GET'])
def getProducts(request):
  products = models.Product.objects.all()
  serializer = serializers.ProductSerializer(products, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
  product = get_object_or_404(models.Product, _id=pk)
  serializer = serializers.ProductSerializer(product, many=False)
  return Response(serializer.data)