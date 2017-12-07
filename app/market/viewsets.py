from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from app.market.models import Category, Goods
from app.market.serializers import CategorySerializer, GoodsSerializer, GoodsDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    ordering_fields = ('price', 'sort_index', 'popularity_index', 'name', )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodsDetailSerializer
        return super(GoodsViewSet, self).get_serializer_class()


class MainGoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodsDetailSerializer
        return super(MainGoodsViewSet, self).get_serializer_class()

    def get_queryset(self):
        return Goods.objects.filter(is_main=True)