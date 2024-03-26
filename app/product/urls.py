from django.urls import path
from .views import *

app_name="product"
urlpatterns=[
    path("",Home,name="home"),
    path("product-detail/<str:id>/<slug:slug>/",product_detail, name="product_detail"),

]