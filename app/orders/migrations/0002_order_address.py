# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес доставки'),
        ),
    ]