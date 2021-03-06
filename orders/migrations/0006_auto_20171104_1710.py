# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-04 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20171104_1710'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_auto_20171103_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custumer_comments',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='productinorder',
            old_name='order_is_active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='order_is_active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='status_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
