# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0035_prestamo_cliente_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_cliente',
            name='date',
            field=models.CharField(db_column='date', max_length=100, null=True, verbose_name='Fecha'),
        ),
    ]
