from django.contrib import admin

from store.models import Category, Product, Order, OrderItem


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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at", "updated_at"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["user"]
    search_fields = ["id", "user__username"]
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product", "quantity", "price", "created_at", "updated_at"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["order", "product"]
