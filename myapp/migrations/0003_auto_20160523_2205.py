# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160523_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='out_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe7\xa6\xbb\xe5\x8e\x82\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xa6\xbb\xe5\x8e\x82'),
        ),
    ]
