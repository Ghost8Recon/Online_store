# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-03 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171103_0422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='is_active',
            new_name='order_is_active',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='is_active',
            new_name='order_is_active',
        ),
    ]