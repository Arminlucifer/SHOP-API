from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class ProductSerializer(serializers.ModelSerializer):

    product_link = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    sale_price = serializers.SerializerMethodField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'product_link',
            'price',
            'sale_price',
            'category',
            'owner',

        ]


    def get_product_link(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)


    def get_sale_price(self, obj):

        return "%.2f" % (float(obj.price) * 1.09)


class ProductDetailSerializer(serializers.ModelSerializer):

    sale_price = serializers.SerializerMethodField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
                 'id',
                'name',
                'price',
                'sale_price',
                'category',
                'owner',

            ]

    def get_owner_username(self, obj):

        if obj.owner:
            return obj.owner.username
        return None

    def get_sale_price(self, obj):
        print(obj.price)
        return "%.2f" % (float(obj.price) * 1.09)