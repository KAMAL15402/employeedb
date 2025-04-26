from django.urls import path
from .views import EmployeeListCreateView, ExportEmployeesCSV
from .views import AttendanceListCreateView



urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/export/', ExportEmployeesCSV.as_view(), name='employee-export'),
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),


]
