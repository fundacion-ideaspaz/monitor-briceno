# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170929_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='completion',
            field=models.CharField(choices=[('Por iniciar', 'Por iniciar'), ('En curso', 'En curso'), ('Terminada', 'Terminada')], default=False, max_length=20, verbose_name='Estado'),
        ),
    ]
