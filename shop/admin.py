from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

class CategorytAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategorytAdmin)
