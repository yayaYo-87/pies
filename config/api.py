from rest_framework.routers import DefaultRouter

from app.market.viewsets import CategoryViewSet, GoodsViewSet, MainGoodsViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)
router.register(r'main_goods', MainGoodsViewSet)
