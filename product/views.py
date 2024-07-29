import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer

# All Products
class ListProducts(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    #The API should also provide the following features:
    #c. Order by property
    #d. Filtering by property(Products)
    filter_backends = [OrderingFilter]

 # Detail Product
class DetailProduct(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
# Update Product
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
# Delete Product
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
 # Create Product
class ProductCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
