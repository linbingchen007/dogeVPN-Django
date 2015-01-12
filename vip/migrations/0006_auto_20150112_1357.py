# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0005_user_rechargetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobVar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autosubavday', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='user',
            name='rechargetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 13, 57, 48, 820000)),
            preserve_default=True,
        ),
    ]
