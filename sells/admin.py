from django.contrib import admin
from sells.models import Client, Product, Category, Proveedor, Sell, Brand


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'code')
    search_fields = ['name']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Client, ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'cost', 'code')
    search_fields = ['name']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Category, CategoryAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'phone')
    search_fields = ['name']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Proveedor, ProveedorAdmin)


class SellAdmin(admin.ModelAdmin):
    list_display = ('id','fecha_pedido', 'cliente', 'total')
    search_fields = ['id', 'fecha_pedido']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Sell, SellAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'code')
    search_fields = ['id', 'name']
    readonly = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldset = ()

admin.site.register(Brand, BrandAdmin)
