# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wotdb_search', '0005_book_chapter_pointofview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointofview',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='pointofview',
            old_name='character_id',
            new_name='character',
        ),
        migrations.AddField(
            model_name='pointofview',
            name='chapter',
            field=models.OneToOneField(null=True,to='wotdb_search.Chapter'),
            preserve_default=False,
        ),
    ]
