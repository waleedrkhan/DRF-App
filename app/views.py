from rest_framework import generics, viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action


class ProductList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        objs = Product.objects.all().values()
        return Response(list(objs))

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        obj = Product.objects.get(pk=kwargs.get('pk', 1))
        out = ProductSerializer(obj)
        return Response(out.data)


# class CartDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#     def post(self, request, pk):
#         prod = Product.objects.get(pk=pk)
#
#     def add(self, request, pk):
#         import pdb;pdb.set_trace()
#         prod = Product.objects.get(pk=pk)
#         Cart(item=prod.pk).save()
#         return Response({"success":True})
