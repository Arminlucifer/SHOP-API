from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework import serializers


from .models import Category, Product
from . validators import validate_name, validate_price


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

    owner = serializers.StringRelatedField(read_only=True)
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators =[validate_name])
    price = serializers.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     validators=[validate_price])
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'email',
            'product_link',
            'price',
            'sale_price',
            'category',
            'owner',


        ]
    # def validate_name(self, name):
    #     if name == '':
    #         raise serializers.ValidationError('Name cannot be empty')
    #     qs = Product.objects.filter(name__iexact=name)
    #     if qs.exists():
    #         raise serializers.ValidationError('Product with this name already exists')
    #     return name
    # def validate_price(self, price):
    #     if price <= 0 :
    #         raise serializers.ValidationError('Price must be greater than 0')
    #     return price
    def create(self, validated_data):
        email = validated_data.pop('email', None)
        print(email)
        instance = super().create(validated_data)
        return instance





    #second method to get product link
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
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators =[validate_name])
    price = serializers.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     validators=[validate_price])

    class Meta:
        model = Product
        fields = [
                 'id',
                'name',
                'email',
                'price',
                'sale_price',
                'category',
                'owner',

            ]

    # def validate_price(self, price):
    #     request = self.context.get('request')
    #     print(request)
    #     if price <= 0:
    #         raise serializers.ValidationError('Price must be greater than 0')
    #     return price
    #
    # def validate_name(self, name):
    #     if name == '':
    #         raise serializers.ValidationError('Name cannot be empty')
    #     qs = Product.objects.filter(name__iexact=name)
    #     if qs.exists():
    #         raise serializers.ValidationError('Product with this name already exists')
    #     return name

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        if email:
            print(f'sending email to {email}')

        return super().update(instance, validated_data)

    def get_owner_username(self, obj):

        if obj.owner:
            return obj.owner.username
        return None

    def get_sale_price(self, obj):
        print(obj.price)
        return "%.2f" % (float(obj.price) * 1.09)