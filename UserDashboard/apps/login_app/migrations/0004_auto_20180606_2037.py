# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-07 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20180606_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(default=2),
        ),
    ]
