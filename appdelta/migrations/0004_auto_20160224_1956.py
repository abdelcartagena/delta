# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0003_login_admin_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos_cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='datos_cliente',
            name='document',
            field=models.CharField(db_column='document', max_length=50, primary_key=True, serialize=False, verbose_name='Documento'),
        ),
    ]
