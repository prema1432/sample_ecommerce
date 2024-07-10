from django.contrib import admin

from store.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "created_at", "updated_at"]
    search_fields = ["name"]
    autocomplete_fields = ["category"]
    list_filter = ["created_at", "category"]
    date_hierarchy = "created_at"
