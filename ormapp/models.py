# models.py
import pandas as pd
from django.db import models


class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience_in_years = models.IntegerField()

    @classmethod
    def display_data(cls, num_records=None):
        employees = cls.objects.all()[:num_records] if num_records else cls.objects.all()
        df = pd.DataFrame(list(employees.values()), index=[f'Record {i+1}' for i in range(len(employees))])
        print(df)

    def __repr__(self):
        return f"Employee(name={repr(self.name)}, age={self.age}, experience_in_years={self.experience_in_years})"
