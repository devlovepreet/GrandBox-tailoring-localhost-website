# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=128)),
                ('customer_phone', models.IntegerField(default=0)),
                ('customer_email', models.EmailField(blank=True, max_length=128)),
                ('customer_age', models.IntegerField(default=0)),
                ('customer_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('customer_details', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=256)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_details', models.CharField(blank=True, max_length=500)),
                ('order_amount', models.IntegerField(default=0)),
                ('order_status', models.CharField(choices=[('1', 'BOOKED'), ('2', 'COMPLETED'), ('3', 'DELIVERED')], default='1', max_length=1)),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]