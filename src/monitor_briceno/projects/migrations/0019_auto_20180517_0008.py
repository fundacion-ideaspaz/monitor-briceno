# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-17 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20180517_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.IntegerField(blank=True, help_text='Cifra en pesos colombianos', null=True, verbose_name='Monto de ejecución'),
        ),
    ]
