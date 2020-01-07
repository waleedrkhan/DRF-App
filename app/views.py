from rest_framework import generics
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
import json


class ProductList(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_list.html'

    def get(self, request, *args, **kwargs):
        objs = Product.objects.all()
        return Response({'products': objs})


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        obj = Product.objects.get(pk=kwargs.get('pk', 1))
        return Response(json.dumps(obj))
