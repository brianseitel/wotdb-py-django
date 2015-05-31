# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wotdb_search', '0002_auto_20150525_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('place_type', models.CharField(max_length=32, null=True, choices=[(b'Country', b'Country'), (b'City', b'City')])),
                ('ruler', models.CharField(default=b'', max_length=100)),
                ('allegiance', models.CharField(default=b'None', max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Sept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('clan', models.OneToOneField(to='wotdb_search.Clan')),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='channeler_type',
            field=models.OneToOneField(null=True, to='wotdb_search.ChannelerType'),
        ),
        migrations.AddField(
            model_name='character',
            name='city',
            field=models.OneToOneField(related_name='city', null=True, to='wotdb_search.Place'),
        ),
        migrations.AddField(
            model_name='character',
            name='clan',
            field=models.OneToOneField(null=True, to='wotdb_search.Clan'),
        ),
        migrations.AddField(
            model_name='character',
            name='country',
            field=models.OneToOneField(related_name='country', null=True, to='wotdb_search.Place'),
        ),
        migrations.AddField(
            model_name='character',
            name='job',
            field=models.OneToOneField(null=True, to='wotdb_search.Job'),
        ),
        migrations.AddField(
            model_name='character',
            name='sept',
            field=models.OneToOneField(null=True, to='wotdb_search.Sept'),
        ),
        migrations.AddField(
            model_name='character',
            name='society',
            field=models.OneToOneField(null=True, to='wotdb_search.Society'),
        ),
    ]
