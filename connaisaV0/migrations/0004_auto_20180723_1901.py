# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-23 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connaisaV0', '0003_auto_20180723_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='student_id',
        ),
        migrations.AddField(
            model_name='history',
            name='student_id',
            field=models.ManyToManyField(to='connaisaV0.user'),
        ),
    ]
