# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_auto_20170928_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(help_text='Ingresar correo con el dominio de la organización.', max_length=255, unique=True),
        ),
    ]