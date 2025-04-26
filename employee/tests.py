from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            department='Engineering',
            salary=70000,
            hire_date='2022-01-01',
            performance_score=8,
            is_active=True
        )
        self.assertEqual(employee.first_name, 'John')
        self.assertEqual(employee.department, 'Engineering')
