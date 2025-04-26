from rest_framework import generics, filters
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from rest_framework.throttling import UserRateThrottle
from django.http import HttpResponse, JsonResponse
import csv


import csv

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'department']
    ordering_fields = ['salary', 'performance_score', 'hire_date']

class ExportEmployeesCSV(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Department', 'Salary', 'Hire Date', 'Performance Score', 'Active'])

        for emp in Employee.objects.all():
            writer.writerow([
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.department,
                emp.salary,
                emp.hire_date,
                emp.performance_score,
                emp.is_active
            ])

        return response
    

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    throttle_classes = [UserRateThrottle]
