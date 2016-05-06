# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_amount_status',
            field=models.CharField(choices=[('1', 'UNPAID'), ('2', 'PAID')], default='1', max_length=1),
        ),
    ]