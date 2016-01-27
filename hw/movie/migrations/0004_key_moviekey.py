# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='moviekey',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
