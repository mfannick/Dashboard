# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-12-02 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0011_auto_20191122_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coverimage',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_page',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]