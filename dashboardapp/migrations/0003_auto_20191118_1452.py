# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-18 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0002_auto_20191118_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='categoryName',
        ),
    ]
