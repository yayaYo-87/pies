from rest_framework import pagination
from rest_framework import serializers
from rest_framework.settings import api_settings

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
            'shot_description',
        ]


class CategoryGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug',]


class GoodsDetailSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(many=True, required=False)
    category = CategoryGoodsSerializer(many=True, required=False)
    goods_consist = GoodsConsistSerialiser(many=True)

    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'articul',
            'price',
            'category',
            'description',
            'shot_description',
            'cover',
            'is_active',
            'is_main',
            'tag',
            'goods_consist',
            'related_goods',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]


class CategorySerializer(serializers.ModelSerializer):
    # goods_categories = GoodsSerializer(many=True, required=False)
    goods = serializers.SerializerMethodField('get_paginated_goods')

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'icon_active', 'goods']

    # def paginated_tracks(self, obj):
    #     goods = Goods.objects.filter(album=obj)
    #     paginator = pagination.PageNumberPagination()
    #     page = paginator.paginate_queryset(goods, self.context['request'])
    #     serializer = GoodsSerializer(page, many=True, context={'request': self.context['request']})
    #     return serializer.data

    def get_paginated_goods(self, obj):
        goods = Goods.objects.filter(category=obj)[:api_settings.PAGE_SIZE]
        serializer = GoodsSerializer(goods, many=True, context={'request': self.context['request']})
        return serializer.data
