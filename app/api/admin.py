from django.contrib import admin
from .models import Product,  Productkx, Orders, Xomashyolar

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name", "slug"]
    search_fields=["name"]

@admin.register(Xomashyolar)
class XomashyolarAdmin(admin.ModelAdmin):
    list_display=["nome", "soni", "narxi", "meter"]
    search_fields=["nome", "soni", "narxi", "meter"]
    
     
@admin.register(Productkx)
class ProductkxAdmin(admin.ModelAdmin):
    list_display=["soni"]
    search_fields=["soni"]

    
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=["soni", "updated", "created"]