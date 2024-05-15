from django.contrib import admin
from .models import Bank, Role, Employee, Salary

class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'branch', 'address', 'established_date', 'created_by', 'updated_by', 'created_at', 'updated_at')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'updated_by', 'created_at', 'updated_at')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_email', 'bank', 'branch', 'role', 'yearly_salary', 'created_by', 'updated_by', 'created_at', 'updated_at')

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'date', 'created_by', 'updated_by', 'created_at', 'updated_at')

# Register your models with the custom admin classes
admin.site.register(Bank, BankAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, SalaryAdmin)
