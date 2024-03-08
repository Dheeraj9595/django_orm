from django.db import models
from django.contrib.auth.models import User
import pandas as pd


class AbstractTable(models.Model):
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='%(class)s_created_by')

    class Meta:
        abstract = True


class Employee(AbstractTable):
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    state = models.CharField(max_length=200, null=True)
    experience_in_years = models.IntegerField()

    @classmethod
    def display_data(cls, num_records=None):
        employees = cls.objects.all()[:num_records] if num_records else cls.objects.all()
        df = pd.DataFrame(list(employees.values()), index=[f'Record {i + 1}' for i in range(len(employees))])
        print(df)

    def __repr__(self):
        return f"Employee(name={repr(self.name)}, age={self.age}, experience_in_years={self.experience_in_years})"
