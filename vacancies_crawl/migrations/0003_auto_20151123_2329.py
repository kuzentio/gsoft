# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_crawl', '0002_vacancy_is_overlap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='is_overlap',
            new_name='is_from_monster',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='is_from_stepstone',
            field=models.BooleanField(default=False),
        ),
    ]
