# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0041_datos_cliente_datelimite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_cliente',
            name='datelimite',
            field=models.CharField(db_column='datelimite', max_length=100, null=True, verbose_name='Fecha limite del pago'),
        ),
    ]
