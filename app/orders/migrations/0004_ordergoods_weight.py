# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20171212_1401'),
        ('orders', '0003_auto_20171211_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='weight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.GoodsWeight', verbose_name='Вес товара'),
        ),
    ]
