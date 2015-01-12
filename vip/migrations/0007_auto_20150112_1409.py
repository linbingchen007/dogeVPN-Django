# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0006_auto_20150112_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='globvar',
            name='currentfg',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='rechargetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 14, 9, 5, 352000)),
            preserve_default=True,
        ),
    ]
