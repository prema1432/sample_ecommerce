from rest_framework import serializers

from store.models import Category, Product, Order, OrderItem


class CategorySerilizers(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=200)
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerilizersGET(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=200)
    class Meta:
        model = Category
        fields = ['name']


class ProductSerilizers(serializers.ModelSerializer):
    category = CategorySerilizersGET()

    class Meta:
        model = Product
        fields = '__all__'
        # depth =1


class ProductSerilizersPOST(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerilizers(serializers.ModelSerializer):
    product = ProductSerilizers()

    class Meta:
        model = OrderItem
        exclude = ["created_at", "updated_at", "order"]
        # fields = '__all__'


class OrderSerilizers(serializers.ModelSerializer):
    order_items = OrderItemSerilizers(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = self.context["request"].data.get("order_items",[])
        print("items_data 1",items_data)
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            print("item_dataitem_data 2",item_data)
            print("6666",item_data['product_id'])
            get_product = Product.objects.filter(id=item_data["product_id"]).first()
            OrderItem.objects.create(order=order,product =get_product, **item_data)

        return order

