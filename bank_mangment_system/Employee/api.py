from rest_framework import viewsets
from .models import Bank, Role, Employee, Salary
from .serializers import BankSerializer, RoleSerializer, EmployeeSerializer, SalarySerializer

class BankApi(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class RoleApi(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class EmployeeApi(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SalaryApi(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
