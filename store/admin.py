from django.contrib import admin
from store.models.customer import Customer

from store.models.product import Product
from store.models.category import Category
from store.models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)