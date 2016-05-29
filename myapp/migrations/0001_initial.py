# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secret_number', models.IntegerField(unique=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81\xe5\x8d\x95\xe5\x8f\xb7')),
                ('car_number', models.CharField(max_length=20, verbose_name=b'\xe8\xbd\xa6\xe5\x8f\xb7')),
                ('queue_number', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe9\x98\x9f\xe5\x8f\xb7\xe7\xa0\x81')),
                ('phone_number', models.CharField(max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('driver_name', models.CharField(max_length=20, verbose_name=b'\xe5\x8f\xb8\xe6\x9c\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('items', models.CharField(max_length=20, verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe7\xa7\x8d\xe7\xb1\xbb')),
            ],
            options={
                'verbose_name': '\u6392\u961f\u4fe1\u606f\u7ef4\u62a4',
                'verbose_name_plural': '\u6392\u961f\u4fe1\u606f\u7ef4\u62a4',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('queue', models.OneToOneField(primary_key=True, serialize=False, to='myapp.Queue')),
                ('water_content', models.FloatField(max_length=10, verbose_name=b'\xe6\xb0\xb4\xe5\x88\x86\xe5\x90\xab\xe9\x87\x8f', blank=True)),
                ('impurity', models.FloatField(max_length=10, verbose_name=b'\xe6\x9d\x82\xe8\xb4\xa8\xe5\x90\xab\xe9\x87\x8f', blank=True)),
                ('whole_rice_rate', models.FloatField(max_length=10, verbose_name=b'\xe6\x95\xb4\xe7\xb1\xb3\xe7\x8e\x87', blank=True)),
                ('lesion', models.FloatField(max_length=10, verbose_name=b'\xe7\x97\x85\xe6\x96\x91', blank=True)),
                ('chalkiness', models.FloatField(max_length=10, verbose_name=b'\xe5\x9e\xa9\xe7\x99\xbd', blank=True)),
                ('out_of_rice_rate', models.FloatField(max_length=10, verbose_name=b'\xe5\x87\xba\xe7\xb1\xb3\xe7\x8e\x87', blank=True)),
                ('mixed', models.FloatField(max_length=10, verbose_name=b'\xe4\xba\x92\xe6\xb7\xb7', blank=True)),
                ('yellow_grain_rice', models.FloatField(max_length=10, verbose_name=b'\xe9\xbb\x84\xe7\xb2\x92\xe7\xb1\xb3', blank=True)),
                ('inspection_creat_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_good', models.BooleanField(default=True, verbose_name=b'\xe5\x90\x88\xe6\xa0\xbc')),
            ],
            options={
                'verbose_name': '\u5316\u9a8c\u4fe1\u606f\u7ef4\u62a4',
                'verbose_name_plural': '\u5316\u9a8c\u4fe1\u606f\u7ef4\u62a4',
            },
        ),
    ]
