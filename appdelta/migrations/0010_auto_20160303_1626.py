# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0009_auto_20160303_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo_cliente',
            old_name='documen',
            new_name='document',
        ),
    ]
