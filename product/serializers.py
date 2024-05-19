from rest_framework import serializers
from .models import *
from itertools import groupby
from django.forms.models import model_to_dict


# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# Product images
class ProductsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = "__all__"


# Product Variant Serializer
class ProductVariantSerializer(serializers.ModelSerializer):
    variant_name_id = serializers.IntegerField(source="variant.id", read_only=True)
    variant_name = serializers.CharField(source="variant_name.name", read_only=True)
    variant_value = serializers.CharField(source="variant_value.value", read_only=True)                 
    product_id = serializers.IntegerField(source="product.id", read_only=True)
    category_id = serializers.IntegerField(source="product.category.id", read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'variant_name_id', 'variant_name', 'variant_value', 'price', 'product_id', 'category_id']


# Variant Combination Serializer
class VariantCombinationSerializer(serializers.ModelSerializer):
    variant_name_id = serializers.IntegerField(source="variant_name.id", read_only=True)
    variant_name = serializers.CharField(source="variant_name.name", read_only=True)
    variant_value = serializers.CharField(source="variant_value.value", read_only=True)                 
    product_id = serializers.IntegerField(source="product.id", read_only=True)
    category_id = serializers.IntegerField(source="product.category.id", read_only=True)

    class Meta:
        model = VariantCombination
        fields = ['id', 'variant_name_id', 'variant_name', 'variant_value', 'price', 'product_id', 'category_id']
        


# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source="category.id", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    brand_id = serializers.IntegerField(source="brand.id", read_only=True)
    brand_name = serializers.CharField(source="brand.name", read_only=True)
    currency_id = serializers.CharField(source="currency.id", read_only=True)
    currency = serializers.CharField(source="currency.name", read_only=True)
    images = ProductsImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    product_variant = ProductVariantSerializer(source="product", many=True)
    variants = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['id', 'category_id', 'category_name', 'brand_id', 'brand_name', 'currency_id',
                'currency', 'uploaded_images', 'name', 'description',  
                'is_available', 'create_time', 'update_time', 'image', 'images', 'product_variant', 'variants']
        
        
    def get_variants(self, obj):
        variants = VariantCombination.objects.filter(product_id=obj.id)
        variant_dict = {}
        for variant in variants:
            if variant.variant_name and variant.variant_name_id not in variant_dict:
                variant_dict[variant.variant_name and variant.variant_name_id] = []
            variant_dict[variant.variant_name and variant.variant_name_id].append(variant)
        result = []
        for variant_name, variant_list in variant_dict.items():
            result.append({
                'variant_group_id': variant.variant_name_id,
                'variant_group_name': str(variant.variant_name),
                'variations': VariantCombinationSerializer(variant_list, many=True).data
            })
        return result  

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            ProductsImage.objects.create(product=product, image=image)

        return product