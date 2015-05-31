# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wotdb_search', '0004_interview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('book', models.OneToOneField(to='wotdb_search.Book')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.OneToOneField(to='wotdb_search.Book')),
                ('character', models.OneToOneField(to='wotdb_search.Character')),
            ],
        ),
    ]
