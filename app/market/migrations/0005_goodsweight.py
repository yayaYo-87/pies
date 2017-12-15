# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_goods_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена даного веса')),
                ('sort_index', models.PositiveIntegerField(default=0, verbose_name='Индекс сортировки')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_weight', to='market.Goods', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Вес и цена товара',
                'verbose_name_plural': 'Вес и цена товара',
                'ordering': ['sort_index'],
            },
        ),
    ]