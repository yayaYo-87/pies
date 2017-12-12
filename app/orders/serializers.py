from rest_framework import serializers

from app.market.models import Goods, GoodsWeight
from app.orders.models import OrderGoods, Cart, Order


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'price', 'category', 'cover', 'title']


class GoodsWeightSerialiser(serializers.ModelSerializer):
    class Meta:
        model = GoodsWeight
        fields = ['id', 'weight', 'price', 'discount_price']


class OrderGoodsSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(read_only=True)
    goods = GoodsSerializer()
    weight = GoodsWeightSerialiser()

    class Meta:
        model = OrderGoods
        fields = ['id', 'goods', 'count', 'price', 'created_at', 'active', 'cart', 'order']

    def to_internal_value(self, data):
        self.fields['goods'] = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())
        self.fields['weight'] = serializers.PrimaryKeyRelatedField(queryset=GoodsWeight.objects.all())
        return super(OrderGoodsSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        ordergoods = OrderGoods(**validated_data)

        request = self.context['request']
        value = request.session.session_key
        cart = Cart.objects.filter(cookie=value).first()
        ordergoods.cart = cart
        ordergoods.save()
        cart.save()

        return ordergoods


class CartSerializer(serializers.ModelSerializer):
    cart_goods = OrderGoodsSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'price', 'total_count', 'cart_goods', ]


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(required=False)
    total_count = serializers.IntegerField(required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            # 'order_status',
            'total_count',
            'address',
            'phone',
            'first_name',
            # 'last_name',
            'email',
            'total',
            'created_at',
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'total_count',
            # 'order_status',
            # 'order_delivery',
            'phone',
            'address',
            'first_name',
            # 'last_name',
            'email',
            'phone',
            'total',
            'created_at',
            'goods',
        ]
