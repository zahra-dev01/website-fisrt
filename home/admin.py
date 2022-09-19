from django.contrib import admin
from .models import *


class ProductVariantInlines(admin.TabularInline):
    model = Variants
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'amount', 'discount', 'total_price', 'create', 'update', 'available')
    list_filter = ('available',)
    list_editable = ('amount',)
    raw_id_fields = ('category',)
    inlines = [ProductVariantInlines]


class VariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'create', 'rate')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variants, VariantAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color)
admin.site.register(Comment, CommentAdmin)

