from rest_framework import serializers

from product.models import Product
from product.models import Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True, many=True)
  categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)
  
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
      'active',
      'categories_id',
      'category'
    ]

    
  def create(Self,validated_data):
    category_data = validated_data.pop('categories_id')
    product = Product.objects.create(**validated_data)
    for category in category_data:
      product.category.add(category)

    return product