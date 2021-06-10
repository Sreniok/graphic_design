# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200308_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='project_information1',
            new_name='project_information',
        ),
        migrations.RemoveField(
            model_name='order',
            name='project_information2',
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name=int),
        ),
    ]