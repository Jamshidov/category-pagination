from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'price', 'created')


admin.site.register(Product, ProductAdmin)
