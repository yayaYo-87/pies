from rest_framework.routers import DefaultRouter

from app.mainpage.viewsets import MainPageViewSet
from app.market.viewsets import CategoryViewSet, GoodsViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'goods', GoodsViewSet)

router.register(r'main_page', MainPageViewSet)
