# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-23 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connaisaV0', '0002_auto_20180723_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
