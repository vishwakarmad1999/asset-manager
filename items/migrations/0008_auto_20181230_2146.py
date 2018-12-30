# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-30 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20181229_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]