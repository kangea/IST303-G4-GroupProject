from django.contrib import admin

from .models import Brand, Product, ProductURL

class ProductURLInLine(admin.TabularInline):
    model = ProductURL
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','brand','SKU','instock','picture_url','price',
        'restock_date','original_release_date']
    inlines = [ProductURLInLine]

admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
