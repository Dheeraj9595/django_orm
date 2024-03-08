# your_app/management/commands/view_employees.py
from django.core.management.base import BaseCommand
from ormapp.models import Employee


class Command(BaseCommand):
    help = 'View all employee records.'

    def handle(self, *args, **options):
        employees = Employee.objects.all()

        if employees:
            self.stdout.write("Employee records:")
            for employee in employees:
                self.stdout.write(
                    f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Experience: {employee.experience_in_years}")
        else:
            self.stdout.write("No employee records found.")
