from django.db import models
from django.utils.safestring import mark_safe

from app.market.models import upload_to


class MainPage(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

class DiscountSlider(models.Model):
    page = models.ForeignKey('MainPage', verbose_name='Страница', related_name='discount_mains')
    name = models.CharField(verbose_name='Название', max_length=128, null=False)
    icon = models.ImageField(verbose_name='Выбрать иконку слайда', blank=True, upload_to=upload_to)
    icon_active = models.ImageField(verbose_name='Выбрать иконку активного слайда', blank=True, upload_to=upload_to)
    discount = models.CharField(verbose_name='Размер скидки', max_length=128)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайд скидки'
        verbose_name_plural = 'Слайды скидки'
        ordering = ['sort_index']


class DiscountSliderGoods(models.Model):
    discount_slider = models.ForeignKey('DiscountSlider', verbose_name='Слайдер', related_name='discount_goods')
    goods = models.ForeignKey('market.Goods', verbose_name='Товар cо скидкой', related_name='slider_goods')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    class Meta:
        verbose_name = 'Товар слайда скидки'
        verbose_name_plural = 'Товары слайда скидки'
        ordering = ['sort_index']


class GoodsPopular(models.Model):
    page = models.ForeignKey('MainPage', verbose_name='Страница', related_name='popular_goods')
    goods = models.ForeignKey('market.Goods', verbose_name='Популярный товар', related_name='slider_popular_goods')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    class Meta:
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'
        ordering = ['sort_index']


class GoodsRapid(models.Model):
    page = models.ForeignKey('MainPage', verbose_name='Страница', related_name='rapid_goods')
    goods = models.ForeignKey('market.Goods', verbose_name='Срочный товар', related_name='slider_rapid_goods')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    class Meta:
        verbose_name = 'Товар "Прямо сейчас"'
        verbose_name_plural = 'Товары "Прямо сейчас"'
        ordering = ['sort_index']


class MainAboutUs(models.Model):
    page = models.ForeignKey('MainPage', verbose_name='Страница', related_name='main_about')
    text_item = models.TextField(max_length=128, verbose_name='Текст "О нас"')
    image = models.ImageField(verbose_name='Выбрать фото "О нас"', blank=True, upload_to=upload_to)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    class Meta:
        verbose_name = 'Пункт "О нас"'
        verbose_name_plural = 'Пункты "О нас"'
        ordering = ['sort_index']


class ExampleImage(models.Model):
    page = models.ForeignKey('MainPage', null=True, blank=False, verbose_name='Фото для примеров блюд', related_name='main_images')
    image = models.ImageField(verbose_name='Изображение', blank=False, upload_to=upload_to)
    sorting = models.PositiveIntegerField(verbose_name='Сортировка', default=0, blank=True)

    class Meta:
        verbose_name = 'Фотография примера наших блюд'
        verbose_name_plural = 'Фотографии примеров наших блюд'
        ordering = ['sorting', ]

    def image_img(self):
        if self.image:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
