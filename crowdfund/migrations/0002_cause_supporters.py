# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfund', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='supporters',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
