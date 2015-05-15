# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150515_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['ordering_number']},
        ),
        migrations.AddField(
            model_name='section',
            name='category',
            field=models.CharField(default='default-category', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 8, 3, 10, 441011, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 8, 3, 14, 320825, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 8, 3, 23, 769013, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 8, 3, 28, 681208, tzinfo=utc), unique=True, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='ordering_number',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='owner',
            field=models.ForeignKey(default='VT user', to='core.User'),
            preserve_default=False,
        ),
    ]
