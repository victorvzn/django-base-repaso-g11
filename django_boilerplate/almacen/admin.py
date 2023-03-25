from django.contrib import admin
from almacen.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'url_image', 'status',)

admin.site.register(Product, ProductAdmin)