from django.urls import path, include
from .views import *
# from rest_framework.routers import DefaultRouter

# routers=DefaultRouter()
# routers.register("order-create", order_create_views, basename="order-create")
# routers.register("product-list", product_list_views, basename="product")


urlpatterns = [
    
    # """ Orders CRUD """
    path("orders/",orders_crud_view),
    # path("order/",order_list_view),
    # path("order/<str:pk>/",order_detail_view),
    # path("order-update/", order_update_view),
    # path("order-create/", order_create_views),
    
    # """ Product CRUD """
    path("product-list/",product_list_views),
    path("product-detail/<str:pk>/",product_detail_view),
    path("product-create/",product_create_views),
    path("product-update/<str:pk>/",product_update_views),
    path("product-delete/<str:pk>/",product_delete_views),
    
    # """ Product Ketadigan Xamashyolar CRUD """
    # """ Xomashyolar CRUD """
    
]
# urlpatterns=routers.urls