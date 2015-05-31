# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wotdb_search', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='alignment',
            field=models.CharField(default=b'Neutral', max_length=32, choices=[(b'Light', b'Light'), (b'Dark', b'Dark'), (b'Neutral', b'Neutral')]),
        ),
        migrations.AddField(
            model_name='character',
            name='allegiance',
            field=models.CharField(default=b'', max_length=32),
        ),
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(default=b'', max_length=16),
        ),
        migrations.AddField(
            model_name='character',
            name='status',
            field=models.CharField(default=b'Unknown', max_length=32, choices=[(b'Alive', b'Alive'), (b'Dead', b'Dead'), (b'Unknown', b'Unknown')]),
        ),
        migrations.AddField(
            model_name='character',
            name='title',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
