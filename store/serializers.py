from rest_framework import serializers

from store.models import Category, Product


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