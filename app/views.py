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
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        results = Product.objects.all()
        output_serializer = self.get_serializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        results = Product.objects.all()
        output_serializer = self.get_serializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)


class CartList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        results = Cart.objects.all()
        output_serializer = self.get_serializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CartDetail(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        results = Cart.objects.all()
        output_serializer = self.get_serializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)

