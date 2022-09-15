from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')
    list_filter = ('create',)


admin.site.register(Category, CategoryAdmin)