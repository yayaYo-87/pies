# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0004_goods_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.CharField(blank=True, max_length=48, null=True, verbose_name='Кука')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Сумма заказа')),
                ('total_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Общее количество товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Номер телефона')),
                ('total', models.PositiveIntegerField(default=0, null=True, verbose_name='Cумма заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('total_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Общее количество продуктов')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_goods', to='orders.Cart', verbose_name='Корзина')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Goods', verbose_name='Товар')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='orders.Order', verbose_name='Заказанный товар')),
            ],
            options={
                'verbose_name': 'Заказаннай товар',
                'ordering': ['id'],
                'verbose_name_plural': 'Заказанные товары',
            },
        ),
    ]