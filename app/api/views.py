from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework import renderers
from rest_framework import permissions, authentication

from rest_framework import viewsets
from rest_framework.mixins import *

from .models import Product, Orders
from .serializers import ProductSerializer, ProductkxSerializer, OrdersSerializer, XomashyolarSerializer
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     GenericAPIView)

"""
permissions.IsAuthenticatedOrReadOnly -> get amal bajariladi ...
list ko'rinishni ko'rish mumkun likin boshqa
amallarni
qila olmaydi 

"""

#  Product list
class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

product_list_views=ProductListView.as_view()

#  Product Detail
class ProductDetailApi(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"
    
product_detail_view=ProductDetailApi.as_view()

# product create
class ProductCreateView(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
product_create_views=ProductCreateView.as_view()
# Product Update
class ProductUpdateView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # slug desak ham bo'ladi urlni to'g'rilab
    lookup_field="pk"
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)

product_update_views=ProductUpdateView.as_view()

#  delete Product
class ProductDestroyViews(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # slug desak ham bo'ladi urlni to'g'rilab
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
product_delete_views=ProductDestroyViews.as_view()
    
    
    


# ====================================================================================================================
# ----------------------------------  Orders VIEWS   ---------------------------------------------------------------
# ====================================================================================================================
""" 
Men class Views dan foydalanishni avzal
bilaman...
chunki juda osan 
...GenericAPIView dan unimli foydalanish uchun
 ListModelMixin-> List ko'rinsh views class
 CreateModelMixin -> cretate yaratish views class
 RetrieveModelMixin->  detail o'qish views class
 UpdateModelMixin -> update o'zgartishish views class
 DestroyModelMixin-> o'chirish views class
"""
class OrderCRUD(GenericAPIView,
                  ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    lookup_field="pk"
    
    # ListModelMixin-> List ko'rinsh views class
    def get(self, request, *args, **kwargs):
        #  RetrieveModelMixin->  detail o'qish views class
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(self, *args, **kwargs)
    
    # CreateModelMixin -> cretate yaratish views class
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # UpdateModelMixin -> update o'zgartishish views class
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # DestroyModelMixin-> o'chirish views class
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
orders_crud_view=OrderCRUD.as_view()

# ====================================================================================================================
# --------------------------------------------------------------------------------------------------------------------
# ====================================================================================================================
# bitta function ko'rinish
"""
  GET - list ko'rinishda
  PUT- update o'zgartirish ko'rinishda
  POST- create yaratish ko'rinishda
  PATCH- update o'zgartirish ko'rinishda
  DELETE -delete  o'chirish ko'rinishda    
"""
# @api_view(["GET","PUT",POST", "PATCH", "DETETE"])
# def OrdersCRUD(request, pk=None, *args, **kwargs):
#     if request.method=="GET":
#         if pk not None:
#            order=get_object_or_404(Orders, id=pk)
#            serializer=OrdersSerializers(order, many=False)
#            return Response(serializer.data)
#         order=Orders.objects.all()
#         serializer=OrdersSerializers(order, many=True)
#         return Response(serializer.data)

#     elif request.method=="POST":
#         serializer=OrdersSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({"invalid xata":"maydonlar mos emas!!!"})
# 
#     elif request.method=="PATCH":
#         order=get_object_or_404(Orders, id=pk)
#         serializer=OrdersSerializers(instance=order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({"invalid xata":"maydonlar mos emas!!!"})
# 
#     elif request.method=="DELETE":
#         if pk is not None:
#             order=get_object_or_404(Orders, id=pk)
#             order.delete()
#             return Response("delete order")


# ====================================================================================================================
# --------------------------------------------------------------------------------------------------------------------
# ====================================================================================================================

"""
Endilikda CRUD amalni 
birnicha function ko'rinishda 
ifodalayman

"""
# @api_view(['POST'])
# def OrderCreateApi(request):
#     data = request.data
    
#     serializer = OrdersSerializers(data=data)
#     if Orders.objects.filter(**data).exists():
#         return Response(status=status.HTTP_403_FORBIDDEN)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['PUT'])
# def update(request, pk):
#     orders = Orders.objects.get(pk=pk)
#     ordersData = OrdersSerializers(instance=orders, data=request.data)

#     if ordersData.is_valid():
#         ordersData.save()
#         return Response(ordersData.data)

#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['PATCH'])
# def order_update_view(request, pk):
#     orders = Orders.objects.get(pk=pk)
#     ordersData = OrdersSerializers(instance=orders, data=request.data, partial=True)

#     if ordersData.is_valid():
#         ordersData.save()
#         return Response(ordersData.data)

#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['GET'])
# def listorderss(request):

#     ordersData = Orders.objects.all()

#     if ordersData:
#         serialzedData = OrdersSerializers(ordersData, many=True)
#         return Response(serialzedData.data)
#     return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['DELETE'])
# def removeorders(request, pk):
#     orders = Orders.objects.get(pk=pk)
#     orders.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)


# ====================================================================================================================
# --------------------------------------------------------------------------------------------------------------------
# ====================================================================================================================
# Order Create Update Delete and List class views 
# "GET", "POST", "PUT", "DETETE"


# GET -List
class OrderListApi(ListAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    
order_list_view=OrderListApi.as_view()

# GET - Retrieve
class OrderDetailApi(RetrieveAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    lookup_field="pk"
    
    
order_detail_view=OrderDetailApi.as_view()

# POST- Create
class OrderCreateApi(CreateAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def perform_create(self, serializer):
    #     serializer.save()
    #     return super().perform_create(serializer)
    
order_create_views=OrderCreateApi.as_view()

# PUT yoke PATCH o'zgartirish
class OrderUpdateApi(UpdateAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    lookup_field="pk"
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
order_update_view=OrderUpdateApi.as_view()

# DELETE- delete destroy  o'chirish
class OrderDeleteApi(DestroyAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer
    lookup_field="pk"
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    
order_delate_view=OrderDeleteApi.as_view()