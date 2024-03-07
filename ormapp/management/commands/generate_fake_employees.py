from django.core.management import BaseCommand
from django.http import HttpRequest
from ormapp.models import Employee
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate and insert 1000 fake employee records'

    def handle(self, *args, **options):
        request = HttpRequest()

        for _ in range(1000):
            Employee.objects.create(
                name=fake.name(),
                age=fake.random_int(min=18, max=60),
                experience_in_years=fake.random_int(min=1, max=10)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated and inserted 1000 fake records.'))
