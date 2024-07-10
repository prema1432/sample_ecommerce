from rest_framework import serializers

from store.models import Category


class CategorySerilizers(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=200)
    class Meta:
        model = Category
        fields = '__all__'
