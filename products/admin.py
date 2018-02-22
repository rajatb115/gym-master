from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    exclude = ['addded']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)