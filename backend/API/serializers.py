from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):

    owner_username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'owner',
            'owner_username',
        ]


    def get_owner_username(self, obj):

        if obj.owner:
            return obj.owner.username
        return None
