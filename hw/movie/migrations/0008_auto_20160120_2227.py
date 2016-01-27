# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20160120_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Time')),
            ],
        ),
        migrations.RemoveField(
            model_name='key',
            name='moviekey',
        ),
    ]
