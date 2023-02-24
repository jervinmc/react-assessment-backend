from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Product
from .serializers import ProductSerializer
from users.models import User
from users.serializers import GetUserSerializer
class ProductView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name']
    queryset=Product.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ProductSerializer


