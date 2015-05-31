# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wotdb_search', '0003_auto_20150525_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(default=b'Robert Jordan', max_length=100)),
                ('question', models.TextField(default=b'')),
                ('answer', models.TextField(default=b'')),
                ('name', models.TextField(default=b'')),
                ('date', models.CharField(default=b'', max_length=32)),
            ],
        ),
    ]
