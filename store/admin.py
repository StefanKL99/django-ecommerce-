from django.contrib import admin
from .models import Category, Customer, Tag, Product, Order, Brand
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Tag)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
admin.site.register(Product)
admin.site.register(Order)