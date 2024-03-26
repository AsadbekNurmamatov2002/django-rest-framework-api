from django.contrib import admin
from .models import Product, Orders, Xomashyolar, Productkx

class ProductKetadiganXomashyoAdmin(admin.TabularInline):
    model=Productkx
    # raw_id_fields=['xomashyolar']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    prepopulated_fields={'slug':('name',)}
    inlines=[ProductKetadiganXomashyoAdmin]
admin.site.register(Xomashyolar)
admin.site.register(Orders)
