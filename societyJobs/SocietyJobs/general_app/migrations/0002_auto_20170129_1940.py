# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-29 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyData',
            new_name='Society_follows',
        ),
    ]
