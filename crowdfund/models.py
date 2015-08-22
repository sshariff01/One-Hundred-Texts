from django.db import models

class Cause(models.Model):
    headline = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=30)
    goal = models.IntegerRangeField(min_value=1, max_value=2147483647)
    supporters = models.PositiveIntegerField

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)