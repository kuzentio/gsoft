# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_crawl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_overlap',
            field=models.BooleanField(default=False),
        ),
    ]
