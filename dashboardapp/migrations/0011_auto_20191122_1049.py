# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-22 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0010_auto_20191122_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='snippet',
            field=models.ImageField(blank=True, null=True, upload_to='question/'),
        ),
    ]