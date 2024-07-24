import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        unique_together = ["category", "name"]


# class

# https://www.amazon.in/Prama-Channel-Required-Accessories-Detection/dp/B0C5TL3JNT/ref=pd_day0_d_sccl_2_1/258-6421061-8835724?pd_rd_w=nZVNj&content-id=amzn1.sym.49a78501-94d9-417e-bc7b-53394962d54d&pf_rd_p=49a78501-94d9-417e-bc7b-53394962d54d&pf_rd_r=9H3ZSTVHVRTDY9PXK4JV&pd_rd_wg=Np4iP&pd_rd_r=cd154631-4dbe-4c07-b2be-c7d9ff740e37&pd_rd_i=B0C5TL3JNT&psc=1


class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100,
                              choices=[("pending", "Pending"), ("shipped", "Shipped"), ("delivered", "Delivered")],
                              default="pending")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # print("items sa",self.order_items.all())
        self.total_price = sum([item.price for item in self.order_items.all()])
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        # self.order.total_price += self.price
        super().save(*args, **kwargs)
        self.order.save()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
