from rest_framework import serializers
from .models import Product, Productkx, Orders, Xomashyolar



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        

class XomashyolarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Xomashyolar
        fields="__all__"
        

class ProductkxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productkx
        fields="__all__"
        

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"