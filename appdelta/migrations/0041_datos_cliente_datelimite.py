# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0040_auto_20160314_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_cliente',
            name='datelimite',
            field=models.IntegerField(db_column='datelimite', null=True, verbose_name='Fecha limite del pago'),
        ),
    ]
