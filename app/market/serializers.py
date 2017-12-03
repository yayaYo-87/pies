from rest_framework import serializers

from app.market.models import GoodsConsist, Tag, Goods, Category


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class GoodsConsistSerialiser(serializers.ModelSerializer):
    class Meta:
        model = GoodsConsist
        fields = ['id', 'text_item', 'sort_index']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'price',
            'cover',
        ]


class CategoryGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug',]


class GoodsDetailSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(many=True, required=False)
    category = CategoryGoodsSerializer(many=True, required=False)

    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'articul',
            'price',
            'category',
            'description',
            'cover',
            'is_active',
            'is_main',
            'tag',
            'related_goods',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]


class CategorySerializer(serializers.ModelSerializer):
    goods_categories = GoodsSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'goods_categories',]
