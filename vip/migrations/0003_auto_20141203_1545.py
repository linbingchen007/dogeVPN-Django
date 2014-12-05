# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0002_auto_20141203_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
