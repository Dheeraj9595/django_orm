# models.py
from django.db import models


class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience_in_years = models.IntegerField()

    def __str__(self):
        return self.name
