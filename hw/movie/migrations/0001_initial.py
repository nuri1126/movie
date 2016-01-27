# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(to='movie.Date')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.ManyToManyField(to='movie.Date', through='movie.Key')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.ManyToManyField(to='movie.Date', through='movie.Key')),
                ('movie', models.ManyToManyField(to='movie.Movie', through='movie.Key')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('key', models.ForeignKey(to='movie.Key')),
            ],
        ),
        migrations.AddField(
            model_name='key',
            name='movie',
            field=models.ForeignKey(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='key',
            name='place',
            field=models.ForeignKey(to='movie.Place'),
        ),
    ]
