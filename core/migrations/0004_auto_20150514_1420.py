# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 14, 14, 20, 22, 438646, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 14, 14, 20, 27, 238592, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
