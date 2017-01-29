# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-29 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20170128_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.SoietyData')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentData')),
            ],
        ),
    ]
