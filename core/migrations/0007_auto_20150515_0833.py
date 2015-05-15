# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150515_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'section_categories',
            },
        ),
        migrations.AlterField(
            model_name='section',
            name='category',
            field=models.ForeignKey(to='core.SectionCategory'),
        ),
    ]
