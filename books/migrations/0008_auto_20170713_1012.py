# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0007_auto_20170712_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Thriller', 'Thriller')], max_length=254),
        ),
    ]
