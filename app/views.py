from rest_framework import generics
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.http import JsonResponse


class ProductList(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        objs = Product.objects.all().values()
        return JsonResponse(list(objs), safe=False)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        obj = Product.objects.get(pk=kwargs.get('pk', 1))
        out = ProductSerializer(obj)
        return Response(out.data)
