# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='queue',
            options={'ordering': ['-out_time'], 'verbose_name': '\u6392\u961f\u4fe1\u606f\u7ef4\u62a4', 'verbose_name_plural': '\u6392\u961f\u4fe1\u606f\u7ef4\u62a4'},
        ),
        migrations.AddField(
            model_name='queue',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 13, 56, 49, 455355, tzinfo=utc), verbose_name=b'\xe8\xbf\x9b\xe5\x8e\x82\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='queue',
            name='out_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 13, 56, 56, 584116, tzinfo=utc), verbose_name=b'\xe5\x87\xba\xe5\x8e\x82\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='queue',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x87\xba\xe5\x8e\x82'),
        ),
        migrations.AlterField(
            model_name='result',
            name='chalkiness',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe5\x9e\xa9\xe7\x99\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='impurity',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe6\x9d\x82\xe8\xb4\xa8\xe5\x90\xab\xe9\x87\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='lesion',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe7\x97\x85\xe6\x96\x91', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='mixed',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe4\xba\x92\xe6\xb7\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='out_of_rice_rate',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe5\x87\xba\xe7\xb1\xb3\xe7\x8e\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='water_content',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe6\xb0\xb4\xe5\x88\x86\xe5\x90\xab\xe9\x87\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='whole_rice_rate',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe6\x95\xb4\xe7\xb1\xb3\xe7\x8e\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='yellow_grain_rice',
            field=models.FloatField(max_length=10, null=True, verbose_name=b'\xe9\xbb\x84\xe7\xb2\x92\xe7\xb1\xb3', blank=True),
        ),
    ]
