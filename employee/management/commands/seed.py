from django.core.management.base import BaseCommand
from faker import Faker
from employee.models import Employee
import random

class Command(BaseCommand):
    help = 'Seed the database with employee data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']

        for _ in range(5):  # Generate 5 employees
            Employee.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.unique.email(),
                department=random.choice(departments),
                salary=random.uniform(50000, 150000),
                hire_date=faker.date_between(start_date='-5y', end_date='today'),
                performance_score=random.randint(1, 10),
                is_active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS(' Successfully seeded the database!'))
