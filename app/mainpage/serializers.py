from rest_framework import serializers

from app.mainpage.models import ExampleImage, GoodsPopular, GoodsRapid, MainAboutUs, DiscountSliderGoods, DiscountSlider, \
    MainPage
from app.market.serializers import GoodsSerializer


class ExampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleImage
        fields = ['id', 'image']


class GoodsPopularSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = GoodsPopular
        fields = ['id', 'goods', 'sort_index']


class GoodsRapidSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = GoodsRapid
        fields = ['id', 'goods', 'sort_index']


class MainAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUs
        fields = ['id', 'text_item', 'image', 'sort_index']


class DiscountSliderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = DiscountSliderGoods
        fields = ['id', 'goods', 'sort_index']


class DiscountSliderSerializer(serializers.ModelSerializer):
    discount_goods = DiscountSliderGoodsSerializer(many=True)

    class Meta:
        model = DiscountSlider
        fields = ['id', 'name', 'icon', 'icon_active', 'discount', 'sort_index', 'discount_goods']


class MainPageSerializer(serializers.ModelSerializer):
    discount_mains = DiscountSliderSerializer(many=True)
    popular_goods = GoodsPopularSerializer(many=True)
    rapid_goods = GoodsRapidSerializer(many=True)
    main_about = MainAboutUsSerializer(many=True)
    main_images = ExampleImageSerializer(many=True)

    class Meta:
        model = MainPage
        fields = ['id', 'name', 'discount_mains', 'popular_goods', 'rapid_goods', 'main_about', 'main_images']
