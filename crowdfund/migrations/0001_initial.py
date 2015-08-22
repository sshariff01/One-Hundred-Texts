# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import crowdfund.custom_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=30)),
                ('goal', crowdfund.custom_fields.IntegerRangeField()),
            ],
        ),
    ]
