from django.contrib import admin
from products.models import *


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInLine]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(Companiya)
admin.site.register(Comment)
admin.site.register(Place)