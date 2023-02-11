from rest_framework import generics
from product.serializer import ProductSerializer
from product.models import Product

class ProductsCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()