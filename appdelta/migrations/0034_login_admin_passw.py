# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdelta', '0033_auto_20160308_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_admin',
            name='passw',
            field=models.CharField(db_column='passw', max_length=200, null=True, verbose_name='Contrasena'),
        ),
    ]