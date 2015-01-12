# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0004_auto_20141203_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rechargetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 13, 12, 57, 135000)),
            preserve_default=True,
        ),
    ]
