# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-03 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171103_0434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product in order', 'verbose_name_plural': 'Products in order'},
        ),
    ]
