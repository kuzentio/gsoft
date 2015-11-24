# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_crawl', '0003_auto_20151123_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
