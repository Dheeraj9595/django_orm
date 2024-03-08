from ormapp.models import Employee
from prettytable import PrettyTable
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Display employee records in a pretty table'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Number of records to display')

    def handle(self, *args, **options):
        # Get the number of records from the command-line argument
        num_records = options['num_records']

        # Get the queryset
        queryset = Employee.objects.all()[:num_records]

        # Create a PrettyTable instance
        table = PrettyTable()

        # Define field names
        table.field_names = ["ID", "Name", "Age", "Experience"]

        # Add rows to the table
        for employee in queryset:
            table.add_row([employee.id, employee.name, employee.age, employee.experience_in_years])

        # Print the table
        self.stdout.write(table.get_string())
        self.stdout.write(self.style.SUCCESS(f'Displayed {num_records} employee records.'))
