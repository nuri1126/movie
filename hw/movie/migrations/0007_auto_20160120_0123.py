# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20160120_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='key',
            new_name='moviekey',
        ),
    ]
