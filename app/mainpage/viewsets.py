from rest_framework import viewsets

from app.mainpage.models import MainPage
from app.mainpage.serializers import MainPageSerializer


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer