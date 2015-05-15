# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150514_1420'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Announcement',
            new_name='Section',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-last_seen', 'joined_date']},
        ),
        migrations.AlterModelTable(
            name='section',
            table='sections',
        ),
    ]
