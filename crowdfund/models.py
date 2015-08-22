from django.db import models

import custom_fields


class Cause(models.Model):
    headline = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=30)
    goal = custom_fields.IntegerRangeField(min_value=1, max_value=2147483647)
    supporters = models.PositiveIntegerField

