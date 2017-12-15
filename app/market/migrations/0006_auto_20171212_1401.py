# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_goodsweight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='price',
        ),
        migrations.AddField(
            model_name='goodsweight',
            name='discount_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='goodsweight',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес товара'),
        ),
    ]