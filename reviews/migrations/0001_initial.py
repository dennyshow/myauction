# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-26 11:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auction', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time_sent', models.DateTimeField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.Auction')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
