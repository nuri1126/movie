# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20160120_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='moviekey',
            new_name='key',
        ),
    ]
