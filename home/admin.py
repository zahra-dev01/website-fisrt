from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'amount', 'discount', 'total_price', 'create', 'update', 'available')
    list_filter = ('available',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)