# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('arquivo', models.FileField(upload_to='musicas/')),
            ],
        ),
    ]
