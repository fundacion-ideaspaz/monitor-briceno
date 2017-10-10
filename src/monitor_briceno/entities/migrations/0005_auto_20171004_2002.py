# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_auto_20171004_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(help_text='Preferiblemente correo institucional.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(max_length=50, verbose_name='Cargo en la organización'),
        ),
    ]