from rest_framework.routers import DefaultRouter

from app.mainpage.viewsets import MainPageViewSet
from app.market.viewsets import CategoryViewSet, GoodsViewSet
from app.orders.viewsets import OrderViewSet, CartViewSet, OrderGoodsViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)

router.register(r'main_page', MainPageViewSet)

router.register(r'order', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'order_goods', OrderGoodsViewSet)
