from rest_framework import serializers
from .models import Product, Productkx, Orders, Xomashyolar



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["name", "image", "slug","productkitadiganxomashyolar", "orders"]
    def create(self, validated_data):
        """ productkitadiganxomashyolar object bulgani uchun (pop) orali olamiz..."""
        productkx=validated_data.pop("productkitadiganxomashyolar")
        qs=Product.objects.create(**validated_data)
        return qs
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
    
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