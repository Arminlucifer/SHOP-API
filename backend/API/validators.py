from rest_framework import serializers

from . models import Product

def validate_name(name):

    if name is None:
        raise serializers.ValidationError('Name cannot be empty')
    qs = Product.objects.filter(name__iexact=name)
    if qs.exists() :
        raise serializers.ValidationError('Product with this name already exists')
    return name
def validate_price(price):
    if price <= 0 :
        raise serializers.ValidationError('Price must be greater than 0')
    return price