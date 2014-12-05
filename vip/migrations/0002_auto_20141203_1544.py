# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(verbose_name=b'heh'),
            preserve_default=True,
        ),
    ]
