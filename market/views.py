from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET', 'POST'])
def index(request, shop_id, category_id):
    if request.method == 'GET':
        data = Product.objects.filter(shop=shop_id, category=category_id)
        serializer = ProductSerializer(data, many=True)
        for a in serializer.data:
            del a['category']
            del a['shop']
            del a['description']
        return Response(serializer.data)
    elif request.method == "POST":
        for a in request.data:
            a["description"] = 'smth'
            a["category"] = category_id
            a["shop"] = shop_id
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def product_detail(request, shop_id, category_id, product_id):
    if request.method == 'GET':
        data = Product.objects.filter(shop=shop_id, category=category_id, pk=product_id)
        serializer = ProductSerializer(data, many=True)
        for a in serializer.data:
            del a['category']
            del a['shop']
            del a['description']
        return Response(serializer.data)
    elif request.method == 'PUT':
        prod = Product.objects.get(id=product_id)
        request.data['description'] = prod.description
        request.data['category'] = prod.category.id
        request.data['shop'] = prod.shop.id
        serializer = ProductSerializer(prod, data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
