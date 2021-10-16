from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'name', 'slug', 'price', 'created')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


