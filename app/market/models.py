import os
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


def upload_to(instance, filename):
    """
    Auto generate name for File and Image fields.
    :param instance: Instance of Model
    :param filename: Name of uploaded file
    :return:
    """
    name, ext = os.path.splitext(filename)
    filename = "%s%s" % (uuid.uuid4(), ext or '.jpg')
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    return os.path.join(basedir, filename[:2], filename[2:4], filename)


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=256)
    slug = models.SlugField(verbose_name='URL', null=True, blank=False)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['sort_index']


class Tag(models.Model):
    name = models.CharField(verbose_name='Название тэга', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class GoodsConsist(models.Model):
    goods = models.ForeignKey('market.Goods', verbose_name='Товар', related_name='goods_consist')
    text_item = models.CharField(max_length=128, verbose_name='Пункт состава')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    class Meta:
        verbose_name = 'Пункт состава'
        verbose_name_plural = 'Пункты состава'
        ordering = ['sort_index']


class Goods(models.Model):
    category = models.ManyToManyField('market.Category', verbose_name='Категория товаров', related_name='goods_categories')

    name = models.CharField(verbose_name='Название', max_length=256)
    articul = models.CharField(verbose_name='Артикул товара', max_length=256, null=True, blank=False)
    price = models.PositiveIntegerField(verbose_name='Цена', blank=False)
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)

    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)
    popularity_index = models.PositiveIntegerField(verbose_name='Индекс популярности', default=0)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_main = models.BooleanField(verbose_name='Выводить на главной', default=False)

    tag = models.ManyToManyField('market.Tag', related_name='goods_tag', verbose_name='Метка')
    related_goods = models.ManyToManyField('market.Goods', verbose_name='Похожие товары', related_name='+', blank=True)

    meta_title = models.CharField(verbose_name='meta title', max_length=200, null=True, blank=True)
    meta_description = models.TextField(verbose_name='meta description', null=True, blank=True)
    meta_keywords = models.TextField(verbose_name='meta keywords', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['sort_index']

