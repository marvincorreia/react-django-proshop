from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
  return Response(['/api/products'])


@api_view(['GET'])
def getProducts(request):
  return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
  for i in products:
    if i['_id'] == pk:
     return Response(i)
  
  return Response(None)