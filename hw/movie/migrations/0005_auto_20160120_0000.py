# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_key_moviekey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='key',
            new_name='moviekey',
        ),
    ]
