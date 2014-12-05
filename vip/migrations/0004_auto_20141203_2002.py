# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0003_auto_20141203_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
